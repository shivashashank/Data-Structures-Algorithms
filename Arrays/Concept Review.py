numbers = [10, 20, 300, 40.5, 50]

# random indexing --> O(1) get items if we know the index !!!

# for i in range(len(numbers)):
#	print(numbers[i]);

# OR

# for ele in numbers:
#	print(ele)

# O(N) search running time
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num

print(maximum)
