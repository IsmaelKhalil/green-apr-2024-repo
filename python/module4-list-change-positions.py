# Swapping attempt 1, will not work
first = input('Enter first number: ')
second = input('Enter second number: ')
print('Before swapping:', first, second)
first = second # first and second now have the same value, and the original value of first is lost
second = first # This will not swap the values, as the previous line gave these identical values
print('After swapping:', first, second)


# Swapping attempt 2, will work
first = input('Enter first number: ')
second = input('Enter second number: ')
print('Before swapping:', first, second)
temporary = first # This will assign temporary with the value given to first
first = second # first and second now have the same value, and the original value of first is lost
second = temporary # This will assign second with the value given to temporary, which is the original value of first
print('After swapping:', first, second)


# Swapping attempt 3, will work
first = input('Enter first number: ')
second = input('Enter second number: ')
print('Before swapping:', first, second)
first, second = second, first # This will properly swap the two values
print('After swapping:', first, second)


# Will also work with lists
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
top_cities[0], top_cities[4] = top_cities[4], top_cities[0]
print(top_cities)


# Sorting list elements
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
top_cities.sort()
print(top_cities)

# Sorting numbers
random_numbers = [2, 5, 0, -3, 4]
random_numbers.sort()
print(random_numbers)

# Sorting numbers in reverse order
random_numbers = [2, 5, 0, -3, 4]
random_numbers.sort(reverse=True)
print(random_numbers)

# Sorting without changing the list itself
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
print(sorted(top_cities))
print(top_cities)