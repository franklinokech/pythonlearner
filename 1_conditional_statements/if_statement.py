my_string = 'behave'

my_len = len(my_string)

res = my_string.startswith('be')

if (res and my_len == 7) or (my_string.startswith('b')):
    print('it starts with be')

elif my_len == 5:
    print('Length greater than 5')
    print('Another statement within elif')

elif my_string.endswith('e'):
    print('ends with e')
    
else:
    print('It does not start with be')
