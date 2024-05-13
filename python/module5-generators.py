# Function becomes a generator with "yield"
def get_number():
    for i in range(1, 4):
        yield i

# Will print <generator object get_number at 0x7fd37a478f20>
print(get_number())

# We can store the generator value in a value. This will add the next value every time it is called. It will print 1, then 2, then 3
generated = get_number()
print(next(generated))
print(next(generated))
print(next(generated))

# If we try to print it a 4th time in the range (1, 4), it will not print the 4th result and instead give an error
# print(next(generated))

# We can also use a for-loop
for x in get_number():
    print(x)

# We can also turn them into a list:
numbers = list(get_number())
print(numbers)