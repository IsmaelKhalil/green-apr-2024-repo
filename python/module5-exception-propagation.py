def get_day(user_info):
    day = int(input('What is the date of your birthday? '))
    user_info.append(day)

def get_month(user_info):
    month = int(input('What is the month of your birthday? (1-12)'))
    user_info.append(month)

def get_year(user_info):
    year = int(input('What is the year of your birthday?'))
    user_info.append(year)

# Exceptions are propagated through functions. It will run through each function within the get_user_bday function, without having to call it within each day / month / year function.
def get_user_bday(user_info):
    try:
        get_day(user_info)
        get_month(user_info)
        get_year(user_info)
        print('Your birthday is', user_info)
    except ValueError:
        print('Sorry, you entered an invalid birthday.')

print('Hello, I will collect some info about your birthday.')
user_info = []
get_user_bday(user_info)