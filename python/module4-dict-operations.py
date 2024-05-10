grades = {}
grades['John'] = 'A-'
grades['Anne'] = 'B'
print(grades)

grades['Anne'] = 'A'
print(grades)

grades.update({'John': 'A'})
print(grades)

len(grades)
if 'John' in grades:
    print('John got:', grades['John'])

del grades['John']
print(grades)

# As of Python 3.6, dictionaries are ordered by default

grades = {}
grades['John'] = 'A-'
grades['Anne'] = 'B'
for grade in grades:
    print(grade)

for grade in grades.keys():
    print(grade)

for grade in grades.values():
    print(grade)

for person, grade in grades.items():
    print(person, 'got', grade)