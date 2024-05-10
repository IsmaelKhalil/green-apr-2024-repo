# Dictionaries are collections used to store key-value pairs.
emails = {
    'Anne Stahl': 'astahl@gmail.com',
    'Peter Small': 'peters@yandex.com',
    'Mark Steel': 'mark@steel.com'
}

print(emails['Mark Steel'])

spanish_animals = {
    'dog': 'el perro',
    'cat': 'el gato',
    'horse': 'el caballo',
    'bird': 'el pajaro'
}

print(spanish_animals['bird'])

# Each key must be unique. Otherwise it will only take the most recent value.
spanish_animals = {
    'dog': 'el perro',
    'cat': 'el gato',
    'horse': 'el caballo',
    'bird': 'el pajaro',
    'bird': 'el ave'
}

print(spanish_animals) # returns 'bird': 'el ave'

# You cannot return a value the same way you can with a key
# print(spanish_animals['el perro']) # Will return an error


# Keys can be strings, integers, or any other mutable data type.
tennis_ranking = {
    1: 'Ashleigh Barty',
    2: 'Naomi Osaka',
    3: 'Simons Halep'
}
print(tennis_ranking)

# However, lists are immutable and will not work as keys
# tennis_ranking = {
#     [1]: 'Ashleigh Barty',
#     [2]: 'Naomi Osaka',
#     [3]: 'Simons Halep'
# }
# print(tennis_ranking) # Will return an error

city_ratings = {
    'Bangkok': [7, 4, 7, 5],
    'Hanol': [7, 6, 4, 5],
    'Manil': [6, 6, 4, 4, 5]
}
print(city_ratings)