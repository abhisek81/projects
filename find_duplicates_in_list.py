def find_dups(arr):
    a = set ()
    dups = set ()
    for i in arr:
        if i in a:
            dups.add(i)
        else:
            a.add(i)
    return list(dups)

arr = list(map(int, input("Enter array elements separated by space: ").split()))
print(find_dups(arr))
