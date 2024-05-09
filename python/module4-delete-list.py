top_cities = ['New York City', 'Los Angeles', 'Singapore', 'Chicago', 'Houston', 'Phoenix']
print(top_cities)
print(top_cities[2]) # Prints Singapore
del top_cities[2] #R Deletes element [2], Singapore
print(top_cities)
print(top_cities[2]) # Prints Chicago since all remaining are shifted to the left

top_cities = ['New York City', 'Los Angeles', 'Singapore', 'Chicago', 'Houston', 'Phoenix']
print(top_cities)
del top_cities[3:] # Deletes element [3] onwards
print(top_cities)

top_cities = ['New York City', 'Los Angeles', 'Singapore', 'Chicago', 'Houston', 'Phoenix']
print(top_cities)
del top_cities[:] # Deletes all elements
print(top_cities)

del top_cities # Deletes the list itself
print(top_cities) # Will give an error