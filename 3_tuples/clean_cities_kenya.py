city_to_check = input('Enter a city')

city_to_check = city_to_check.title()

clean_cities = [
    'Nakuru',
    'Eldoret',
    'Kisumu',
    'Mombasa',
    'Meru'
]

for a_city in clean_cities:
    if a_city == city_to_check:
        print('City is clean')
        continue
    else:
        print('City is not clean')

print('Goodbye')
