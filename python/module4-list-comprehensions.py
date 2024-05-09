numbers = [1, 2, 3, 4]

# If we want to add a large quantity of numbers to a list, typing manually will take a long time
# Instead can we use a for-loop. This will take up a lot of space
numbers = []
for i in range(1, 101):
    numbers.append(i)
print(numbers)

# Here is a simplified approach:
numbers = [i for i in range(1, 101)]
print(numbers)

# If we want to skip numbers divisible by 3
numbers = [i for i in range(1, 101) if i % 3 != 0]
print(numbers)