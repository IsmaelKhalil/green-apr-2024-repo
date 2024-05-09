# Lists can have other lists as elements
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
print(cells[0])
print(cells[0][0])
print(cells[0][1])
print(cells[1][2])

# Iterating within the list
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for x in cells:
    print('Element:', x)


# Iterating within each nested list
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for x in cells:
    for y in x:
        print('Element:', y)

# Renaming to resemble Excel
table = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for row in table:
    for cell in row:
        print('Element:', cell)

# Print elements to resemble a table
table = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for row in table:
    for cell in row:
        print(cell, '', end='')
    print()

# If we have multiple rows with the following elements:
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
# Print the list 4 times
table = [[i for i in range(1, 6)] for j in range(4)]
print(table)