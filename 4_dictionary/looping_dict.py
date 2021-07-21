student_details = {
    'name': 'Franklin',
    'faculty': 'CI',
    'age': 26,
    'location': 'Kisumu',
}

# loop,
for i in student_details.keys():
    if i.startswith('a'):
        print(i)