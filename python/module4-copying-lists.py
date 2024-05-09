# name_original and name_new will share values, but will not be linked together.
# Changing one will not affect the other
name_original = 'Jon Snow'
name_new = name_original
name_original = 'Daenerys Targaryen'
print(name_original, name_new)

# This will not apply to lists, as changing one will affect the other
# The reason is because the name of the list references where the list is stored.
list_original = [1, 2, 3]
list_new = list_original
list_original[0] = -5
print('Original:', list_original, '\nNew:', list_new)

# If we want to copy a list, we can use slicing on the original list: list_original[:]
list_original = [1, 2, 3]
list_new = list_original[:]
list_original[0] = -5
print('Original V2:', list_original, '\nNew V2:', list_new)

# You can also do this with ranges
list_original = [1, 2, 3]
list_new = list_original[:2]
list_original[0] = -5
print('Original V2:', list_original, '\nNew V2:', list_new)
