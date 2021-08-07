clean_cities = [
    'Kisumu',
    'Mombasa',
    'Eldoret',
    'Nairobi'
]

city_to_check = input('Enter a city name')

for a_city in clean_cities:
    if city_to_check == a_city:
        print('it is one of the clean cities')
        break
    else:
        print('It is NOT one of the clean cities')
        
