first_names = [
    'franklin',
    'bavon',
    'hunaina',
    'elizabeth',
    'osca',
]

last_names = [
    'okech',
    'okeyo',
    'athman',
    'lanyo',
    'otieno',
]

full_names = []

for a_first_name in first_names:
    for a_last_name in last_names:
        full_names.append(a_first_name+ ' '+a_last_name)

print(full_names)
print(len(full_names))