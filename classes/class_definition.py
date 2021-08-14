class Patient:
    def __init__(self, last_name, first_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def check_if_minor(self):
        if self.age > 21:
            print('Is Not a Minor')
        else:
            print('Is a minor')


pid124 = Patient('Okech', 'Franklin', 19)

print(pid124.last_name)
