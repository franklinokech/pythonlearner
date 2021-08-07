clean_cities = [
    'Kisumu',
    'Mombasa',
    'Eldoret',
    'Nairobi'
]

user_input = ''
while user_input != 'q':
    user_input = input('Enter a city or q to quit')
    for a_city in clean_cities:
        if user_input == a_city:
            print('The city is among the clean cities')
            break
        else:
            print('That is is not clean')