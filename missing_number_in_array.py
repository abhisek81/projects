def missing_number(nums: list[int]):
    nums_set = set(nums)
    n = len(nums)

    for i in range(n+1):
        if i not in nums_set:
            return i
        

nums = list(map(int, input("Enter the array: ").split()))
print(missing_number(nums))

#Enter the array: 1 2 0 -> 3