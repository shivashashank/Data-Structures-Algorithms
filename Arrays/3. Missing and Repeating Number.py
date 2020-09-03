# Problem Link: https://www.geeksforgeeks.org/find-a-repeating-and-a-missing-number/
# Optimal Solution -> XOR / using two equations

# Naive approach
# Time complexity is O(nlogn)
# Space complexity is O(1)

a = [3, 1, 3]
rep, miss = 0, 0
a.sort()
for i in range(len(a)-1):
	if a[i] == a[i+1]:
		rep = a[i]

for i in range(len(a)):
	if i+1 != a[i]:
		miss = i+1

print(f'Repeated number: {rep}', end=' ')
print(f'Missing number: {miss}')

# using Frequency array/Hashmap
# Time complexity is O(n)
# Space complexity is O(n)

a = [3, 1, 3]
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
		print(f'Repeated number: {key}')
	elif value <= 0:
		print(f'Missing number: {key}', end=' ')

# using two equations
# Time complexity is O(n)
# Space complexity is O(1)

a = [3, 1, 3]
n = len(a)
sum_n = n*(n+1)//2
sum_nsq = n*(n+1)*(2*n+1)//6

for i in range(n):
	sum_n -= a[i]
	sum_nsq -= a[i]*a[i]
miss = (sum_n+sum_nsq//sum_n)//2
rep = miss - sum_n
print(f'Repeated number: {rep} Missing number: {miss}')