# Defining a variable inside the scope of a function will work.
# def show_truth():
#     mysterious_var = 'Surprise!'
#     print(mysterious_var)

# show_truth()

# Defining a variable outside the scope of a function will also work if we define it beforehand.
# def show_truth():
#     print(mysterious_var)

# mysterious_var = 'Surprise!'
# show_truth()

# mysterious_var is based to the scope.
# The 'New Surprise!' is local to the function, and the 'Surprise!' is global.
# The local mysterious_var shadows the global, creating a temporary local variable with the same name.
# This is to prevent functions written by other people from being modified accidentally.
# If we add the "global" keyword, it will change the variable outside the function; generally rarely used.
def show_truth():
    global mysterious_var
    mysterious_var = 'New Surprise!'
    print(mysterious_var)

# mysterious_var = g'Surprise!'
# print(mysterious_var)
# show_truth()
# print(mysterious_var)

# If we append a value, we are not creating a local version of the variable, meaning that the method affects the global variable. If we assign it to a new variable, this will not happen.
# def show_truth():
#     mysterious_var.append(['New Surprise!'])
#     print(mysterious_var)

mysterious_var = ['Surprise!']
print(mysterious_var)
show_truth()
print(mysterious_var)

