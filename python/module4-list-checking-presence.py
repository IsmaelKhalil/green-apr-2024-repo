# "in" can be used to check the range of values in a control variable (loops)
for char in 'happy message':
    print(char)

# "in" can also be used to check if a value is present
invited_guests = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie']
name = input('What is your name? ')
if name in invited_guests:
    print('Welcome!')
else:
    print('You are not invited')

# Can also use "not in" as an inverted function

# "in" can also be used to check if a value is present
invited_guests = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie']
name = input('What is your name? ')
if name not in invited_guests:
    print('You are not invited')
else:
    print('Welcome!')