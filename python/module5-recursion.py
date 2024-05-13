# Functions can call themselves.
# We will test it with factorials: 3! = 3 * 2 * 1


# Iterative
def get_factorial(number):
    factorial = 1
    for x in range(1, number + 1):
        factorial *= x
    return factorial
    
print(get_factorial(6))

# Recursive
def get_factorial_recursive(number):
    if number <= 1:
        return 1
    return number * get_factorial_recursive(number - 1)
    
# The way it works:
# 6 * get_factorial_recursive(5) -->
# 5 * get_factorial_recursive(4) -->
# 4 * get_factorial_recursive(3) -->
# 3 * get_factorial_recursive(2) -->
# 2 * get_factorial_recursive(1)
print(get_factorial_recursive(6))