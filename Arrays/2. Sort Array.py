# Problem Link: https://leetcode.com/problems/sort-colors/
# Optimal Solution -> Dutch National Flag algorithm

# Naive approach
# Time complexity is O(nlogn)
# Space complexity is O(1)

a = [2,0,2,1,1,0]
a.sort()
print(a)

# using counting sort/two pass algorithm
# Time complexity is O(n) (actually first pass:O(n) + second pass:O(n) = O(2n))
# Space complexity is O(1)

a = [2,0,2,1,1,0]
count0 = 0
count1 = 0
count2 = 0

for ele in a:
	if ele == 0:
		count0 += 1
	elif ele == 1:
		count1 += 1
	elif ele == 2:
		count2 += 1
i = 0
while count0 > 0 :
	a[i] = 0
	i += 1
	count0 -= 1
while count1 > 0 :
	a[i] = 1
	i += 1
	count1 -= 1
while count2 > 0 :
	a[i] = 2
	i += 1
	count2 -= 1
print(a)

# Dutch Nation Flag algorithm
# Time complexity is O(n)
# Space complexity is O(1)

a = [2,0,2,1,1,0]
low = 0
mid = 0
high = len(a)-1

while mid<=high:
	if a[mid] == 0:
		a[low], a[mid] = a[mid], a[low]
		low += 1
		mid += 1
	elif a[mid] == 1:
		mid += 1
	elif a[mid] == 2:
		a[mid], a[high] = a[high], a[mid]
		high -= 1
print(a)
