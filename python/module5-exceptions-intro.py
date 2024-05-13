# Syntax and Value Errors are exceptions
# An exception is an event which occurs during the execution of a program that disrupts the normal flow of the program's instructions.
# To handle exceptions, we'll use Try-Except

try:
    value = int(input('Enter an integer: '))
    print('The inverse of', value, 'is', 1/value)
except ValueError:
    print('This is not a number.')
except ZeroDivisionError:
    print('You can\'t divide by 0!')
except:
    print('An unknown error occurred.')
    
# Note that you can only catch a SyntaxError if you raise it manually:
try:
    raise SyntaxError
except:
    print('Caught the error')
    
# If your code has a SyntaxError raised by Python automatically, you cannot catch it.
# try:
#     5:4
# except:
#     print('Caught the error')