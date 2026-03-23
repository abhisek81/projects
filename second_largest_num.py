def find_second_largest(nums: list) -> int:
	# write your code here
	first = None
	second = None
	for num in nums:
		if first is None or num > first:
			second = first
			first = num
		elif num < first and (second is None or num > second):
			second = num
	if second is None:
		return None
	return second

print(find_second_largest([9,7,7,6,8]))