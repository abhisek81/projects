def find_dups(arr):
    seen = set ()
    dups = set ()
    for i in arr:
        if i in seen:
            dups.add(i)
        else:
            seen.add(i)
    return list(dups)

arr = list(map(int, input("Enter array elements separated by space: ").split()))
print(find_dups(arr))
