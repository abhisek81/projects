def twoSum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
            
print(twoSum([2,7,11,15], 9))   # [0, 1]
print(twoSum([3,2,1,4], 6))       # [1, 3]
print(twoSum([3,3], 6))         # [0, 1]