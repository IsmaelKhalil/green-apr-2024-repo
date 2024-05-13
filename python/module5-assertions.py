# Assertions are assumptions in our program that should always be true.
def calculate_inverse(number):
    assert(number != 0), 'The number is 0!'
    return 1/number
    
calculate_inverse(0) # Will give us the custom exception AssertError: The number is 0

# Asserts are used for testing and debugging code, as well as to document code.
# Asserts are NOT used to validate user input, as it is possible to turn off assertions when publishing a program to your users, causing you to lose all the code that validates user input.
# Asserts are NOT used for error-handling, because you will want to fix these issues rather than handle them.