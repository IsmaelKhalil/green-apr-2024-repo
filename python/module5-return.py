# The return keyword will return a meaningful value
def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    return average

print('The average is', get_average([5.0, 3.5, 7.8, 9.9, 10.0]))

average = get_average([5.0, 3.5, 7.8, 9.9, 10.0])
if average > 5.0:
    print('The average is too high!')

# The return key will terminate the function, and nothing after it will work.
def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    return average
    print('Show me the average') # This print statement will not run due to the return.
    
print(get_average((2, 3)))

def is_first_last_equal(number_list):
    if len(number_list) == 0:
        return
    if (number_list[0] == number_list[-1]):
        return True
    else:
        return False

# Will return True
print(is_first_last_equal([10, 20, 30, 40, 10]))

# Will return False
print(is_first_last_equal([10, 20, 30, 40, 50]))

# Will return None because the list is empty
print(is_first_last_equal([]))