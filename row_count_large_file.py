import pandas as pd

def count_rows(file_path,chunk_size=10000):
    total = 0

    for chunk in pd.read_csv(file_path,chunksize=chunk_size):
        total+=len(chunk)

    return total

file_path = "/abc/asd/file1.csv"
print("Total row_count :" , count_rows(file_path))