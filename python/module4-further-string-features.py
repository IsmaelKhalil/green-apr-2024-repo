fav_band = 'Sabaton'
print(fav_band[4]) # Will print t

print(fav_band[:4]) # Will print Saba

text = 'please capitalize me'
text_cap = text.upper()
print(text_cap) # PLEASE CAPITALIZE ME

user_number = input('Please provide a number: ')
if user_number.isnumeric():
    print('Thank you, that\'s a correct number!')
else:
    print('Sorry,', user_number, 'is not a number.')