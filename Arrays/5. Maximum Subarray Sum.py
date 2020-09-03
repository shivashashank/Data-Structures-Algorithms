# Problem Link: https://leetcode.com/problems/maximum-subarray/
# Optimal Solution -> Kadane's Algorithm

# Naive approach
# Time complexity is O(n^3)
# Space complexity is O(1)

nums = [-2,1,-3,4,-1,2,1,-5,4]
maxi = nums[0] # atleast one number

for i in range(len(nums)): # for iterating through each ele in list
	for j in range(i, len(nums)): # for generating the sub arrays
		sum_nums = 0
		for k in range(i, j+1): # for iterating through the sub arrays
			sum_nums += nums[k]
			if sum_nums > maxi:
				maxi = sum_nums
print(maxi)

# 
# Time complexity is O(n^2)
# Space complexity is O(1)

nums = [-2,1,-3,4,-1,2,1,-5,4]
maxi = nums[0]

for i in range(len(nums)):
	sum_nums = 0
	for j in range(i, len(nums)):
		sum_nums += nums[j]
		if sum_nums > maxi:
			maxi = sum_nums
print(maxi)

# Kadane's Algorithm
# Time complexity is O(n)
# Space complexity is O(1)

nums = [-2,1,-3,4,-1,2,1,-5,4]
maxi = nums[0]
sum_nums = 0

for i in range(len(nums)):
	sum_nums += nums[i]
	if sum_nums > maxi:
		maxi = sum_nums
	if sum_nums < 0:
		sum_nums = 0
print(maxi)