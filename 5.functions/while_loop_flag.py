clean_cities = [
    'Kisumu',
    'Mombasa',
    'Eldoret',
    'Nairobi'
]

keep_looping = True
while keep_looping:
    user_input = input('Enter name of a city OR q to quit')
    if user_input != 'q':
        for a_city in clean_cities:
            if user_input == a_city:
                print('The city is clean')
                break
            else:
                print('The city is NOT clean')

    else:
        keep_looping = False
