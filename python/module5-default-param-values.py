# print('Hello', 'How are you?', end=',', sep='-')

def print_letter_count(text='This is the default string to search.', letter='a'):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)
    
print_letter_count('How many letter a\'s are there?')


# If a default parameter is used, it must appear at the end
# The line below will not work.
# print_letter_count(letter='a', 'How many letter a\'s are there?')

# The line below will work.
# print_letter_count('How many letter a\'s are there?', letter='a')