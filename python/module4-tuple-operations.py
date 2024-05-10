user_data = ('John', 'American', 1964)
print(len(user_data))

user_data = ('John', 'American', 1964)
if 'American' in user_data:
    print('This person comese from the US.')

user_data = ('John', 'American', 1964)
for element in user_data:
    print(element)

# Behind the scenes, we are getting a new tuple rather than changing the existing tuple
user_data = ('John', 'American', 1964) + ('teacher', 'male')
print(user_data)

numbers = (0, 1) * 10
print(numbers)

# Lists are used when you want many values of the same data type, i.e. same phenomenon
male_names = ['Adam', 'Jerry', 'Mark']
temperatures = [50.1, 53.6, 78.4]

# Tuples are used when you want many values that are different data types that
# are related and form a structure
user_data = ('John', 'American', 1964)

# Also used to perform certain Python operations quicker, such as swapping lists
first = 5
second = 7
first, second = second, first