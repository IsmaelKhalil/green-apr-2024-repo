# Tuples use () while lists use []
empty_tuple = ()
one_el_tuple_a = (1,)
one_el_tuple_b = 1,
three_el_tuple = 1, 2, 3,

print(three_el_tuple)

# Lists are mutable (can modify, add or remove elements)
# Tuples are immutable, and stay unchanged.
# However, you can assign a new tuple to an existing variable.

user_data = ('John', 'American', 1964)
user_data = ('Katya', 'Russian', 1980)

user_data.append('teacher') # Will result in an error, append doesn't exist for tuple
del user_data[0] # Will result in an error, cannot delete

# Strings are similar to Tuples in this regard

message = 'welcome'
message = 'Welcome!'
message[0] = 'w' # Will result in an error, Strings do not support item assignment