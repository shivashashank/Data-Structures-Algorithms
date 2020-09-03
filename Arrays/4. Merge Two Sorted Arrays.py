# Problem Link: https://www.geeksforgeeks.org/efficiently-merging-two-sorted-arrays-with-o1-extra-space/
# Optimal Solution -> Gap algorithm / using insertion kind of algorithm

# Naive approach
# Time complexity is O(nlogn)
# Space complexity is O(n)

a1 = [10]
a2 = [2, 3]
l = []
for ele in a1:
	l.append(ele)
for ele in a2:
	l.append(ele)

l.sort()

for i in range(len(a1)):
	a1[i] = l[i]
for i in range(len(a1), len(a1)+len(a2)):
	a2[i-len(a1)] = l[i]
# OR
'''
n1 = len(a1)
n2 = len(a2)
i, j = 0, 0
while n1 > 0:
	a1[i] = l[i]
	n1 -= 1
	i += 1
while n2 > 0:
	a2[j] = l[j+len(a1)]
	n2 -= 1
	j += 1
'''
print(a1, a2)

# using insertion kind of algorithm
# Time complexity is O(m*n)
# Space complexity is O(1)

a1 = [1, 5, 9, 10, 15, 20]
a2 = [2, 3, 8, 13]

for i in range(len(a1)):
	if a1[i] > a2[0]:
		a1[i], a2[0] = a2[0], a1[i]
		first = a2[0]
		k = 1
		while(k < len(a2)) and (a2[k] < first):
			a2[k-1] = a2[k]
			k += 1
		a2[k-1] = first
print(a1, a2)

# Gap algorithm
# Time complexity is O(nlogn)
# Space complexity is O(1)

