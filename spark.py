def twoSum(nums, target):
    # Loop through each number using index i
    for i in range(len(nums)):
        # Loop through the numbers that come after nums[i]
        for j in range(i + 1, len(nums)):
            # Check if the two numbers add up to the target
            if nums[i] + nums[j] == target:
                return [i, j]
            
print(twoSum([2,7,11,15], 9))   # [0, 1]
print(twoSum([3,2,1,4], 6))       # [1, 2]
print(twoSum([3,3], 6))         # [0, 1]