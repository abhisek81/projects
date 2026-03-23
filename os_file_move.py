# Make a list of all available distinct props.
# Read the config file and discard the inactive props , make a list of active props.

# For each active prop ->
#     check file count , time diff between 1st & last file.
#     count < 55 , time diff < 20H -> Dont do anything , continue
#     count < 55 , time diff > 20H -> Move files to Partial Path
#     count >= 55 ->
# 	    remove dups(check against the config file to remove duplicates) ->
# 		    count = 55 -> Full
# 		    count < 55 , time diff < 20H -> Dont do anything , continue
# 		    count < 55 , time diff > 20H -> Move files to Partial Path
# 		    else Move files to Partial Path


from pathlib import Path
from datetime import datetime
from collections import defaultdict

base = Path("/app/analytics/inbounds/opera/cloud/landing/rna")
config_path = Path("/app/analytics/configs/opera_property_config.cfg")
unique_file_config = Path("/app/analytics/configs/unique_file_config.cfg")
inactive_dir = Path("/app/analytics/inbounds/opera/cloud/landing/inactive_prop_files")
partial_dir = Path("/app/analytics/inbounds/opera/cloud/landing/partialextracts")
full_dir = Path("/app/analytics/inbounds/opera/onprem/landing")

inactive_dir.mkdir(parents=True, exist_ok=True)
partial_dir.mkdir(parents=True, exist_ok=True)
full_dir.mkdir(parents=True, exist_ok=True)

# Read active properties
active_props = set()
with open(config_path, 'r') as f:
    for line in f:
        prop = line.strip().split(',')[0]
        if prop:
            active_props.add(prop)
print(f"Loaded {len(active_props)} active properties\n")

# Read valid file types
valid_file_types = set()
with open(unique_file_config, 'r') as f:
    for line in f:
        line = line.strip()
        if line:
            valid_file_types.add(line)
print(f"Loaded {len(valid_file_types)} valid file types from config\n")

# Find distinct properties and move inactive ones
files = base.glob("*.txt")
distinct_props = set()
for p in files:
    prop = p.name.split("_", 1)[0]
    distinct_props.add(prop)

inactive_props = distinct_props - active_props
for prop in inactive_props:
    for p in base.glob(f"{prop}_*.txt"):
        p.rename(inactive_dir / p.name)
print(f"Moved {len(inactive_props)} inactive properties\n")

# Process active properties
available_active_props = distinct_props & active_props

for prop in available_active_props:
    prop_files = list(base.glob(f"{prop}_*.txt"))
    if not prop_files:
        continue

    valid_entries = []      # (path, type, timestamp)
    timestamps = []

    for p in prop_files:
        parts = p.stem.split('_')
        if len(parts) < 4:
            continue
        file_type = '_'.join(parts[1:-2])
        ts = datetime.strptime(f"{parts[-2]}_{parts[-1]}", "%Y%m%d_%H%M%S")

        if file_type in valid_file_types:
            valid_entries.append((p, file_type, ts))
            timestamps.append(ts)
        else:
            p.rename(partial_dir / p.name)            # invalid type -> partial

    # group by type and drop older duplicates
    kept = []
    by_type = {}
    
    # Step 1: Group files by their type
    for p, ft, ts in valid_entries:
        if ft not in by_type:
            by_type[ft] = []
        by_type[ft].append((p, ts))
    
    # Step 2: For each type, keep newest and move older ones
    for ft in by_type:
        files_list = by_type[ft]
        
        # Find the newest file
        newest_file = None
        newest_time = None
        
        for p, ts in files_list:
            if newest_time is None or ts > newest_time:
                newest_file = p
                newest_time = ts
        
        # Keep newest, move all others
        kept.append(newest_file)
        for p, ts in files_list:
            if p != newest_file:
                p.rename(partial_dir / p.name)

    file_count = len(kept)
    if timestamps:
        time_diff_hours = (max(timestamps)-min(timestamps)).total_seconds()/3600
    else:
        time_diff_hours = 0

    if file_count == 55:
        action = "FULL"
    elif file_count < 55 and time_diff_hours < 20:
        action = "WAIT"
    else:
        action = "MOVE_TO_PARTIAL"

    if action == "FULL":
        for p in kept:
            p.rename(full_dir / p.name)
    elif action == "MOVE_TO_PARTIAL":
        for p in kept:
            p.rename(partial_dir / p.name)

    print(f"{prop:15} | count={file_count:3} | time_diff={time_diff_hours:6.1f}h | {action}")






