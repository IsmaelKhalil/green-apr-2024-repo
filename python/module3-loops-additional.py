# Does not do anything, pass can be used as a placeholder to prevent code from throwing errors
for i in range(11):
    pass

# Multiplication table with nested for-loop
for a in range(1,6):
    for b in range(1,6):
        print(a, 'x', b, '=', a * b)

# For and While can use else clauses, but these are rarely used. Else always executes regardless of result, unlike a break statement is used
i = 2
while i < 5:
    print(i)
    i += 1
else:
    print('else:', i)