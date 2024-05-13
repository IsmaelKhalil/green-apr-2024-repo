# Python has over 60 exception types
# BaseException: template for internal Python exceptions
# - SystemExit: raised when called a special method: sys.exit(), to close the program (can only be used by importing sys)
# - KeyboardInterrupt: raised when user presses a key combination that causes an interrupt to the executing script (such as terminating a program while it's running)
# - Exception: template for internal Python exceptions + your custom exceptions
# -- ArithmeticError, LookupError, TypeError, ValueError
# --- ZeroDivision Error, IndexError, KeyError

# IndexError occurs with a list index out of range
# KeyError occurs with dictionaries, searching for a Key that doesn't exist
# TypeError is when a value type is incompatible, like trying to concatenate string and int
# ValueError: value type is invalid

# Python tries to raise the most specific / applicable error, such as ZeroDivisionError