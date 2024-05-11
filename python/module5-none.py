# Print doesn't return a value, just causes the effect of printing to a console
print('Hello')

# Len doesn't count an effect, but it returns a value
length = len('Hello')

# Input does both: causes an effect (prompts the user) and returns the value given
number = input('What is the number? ')

# This will return "None", which is a null value. It is not empty, zero, or false.
print_return = print('Hello world')
print(print_return)

# "else" will be printed
x = None
if x:
    print('None is true')
elif x is False:
    print('None is false')
else:
    print('None is not true or false, None is just None')

if x is None:
    print('X is None')
if x == None:
    print('X == None')

def greet():
    print('Hello')

x = greet()
print(x)