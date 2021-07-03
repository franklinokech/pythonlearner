tasks = [
    'Email Frank',
    'Call Sarah',
    'Meet with Bavon',
    'Meet Hunaina',
    'Call Bill',
    25,
    4.884,
]

for task in tasks:
    if type(task) is str:
        print(task.upper())
    else:
        print(task)
