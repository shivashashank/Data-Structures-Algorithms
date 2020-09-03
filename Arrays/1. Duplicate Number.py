# Problem Link: https://leetcode.com/problems/find-the-duplicate-number/solution/
# Optimal Solution -> Floyd's Tortoise and Hare algorithm

# Naive approach
# Time complexity is O(nlogn)
# Space complexity is O(1)

a = [1,3,4,2,2]
a.sort()
for i in range(len(a)-1):
	if a[i] == a[i+1]:
		res = a[i]
print(res)

# using Frequency array/Hashmap
# Time complexity is O(n)
# Space complexity is O(n)

a = [1,3,4,2,2]
freq = {}
for i in range(1, len(a)+1):
	freq[i] = 0
for ele in a:
	if ele in freq:
		freq[ele] += 1
	else:
		freq[ele] = 1
for key, value in freq.items():
	if value >= 2:
		print(key)

# Floyd's Tortoise and Hare algorithm
# Time complexity is O(n)
# Space complexity is O(1)

a = [1,3,4,2,2]
slow = a[0]
fast = a[a[0]]
while(slow != fast):
	slow = a[slow]
	fast = a[a[fast]]
fast = 0
while(slow != fast):
	slow = a[slow]
	fast = a[fast]
print(slow)