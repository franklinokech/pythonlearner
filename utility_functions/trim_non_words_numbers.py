test_string = 'Three Months'
test_string = test_string.lower()

# singles
units = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
    "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
    "sixteen", "seventeen", "eighteen", "nineteen",
]

# tens
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

# larger scales
scales = ["hundred", "thousand", "million", "billion", "trillion"]

test_string_list = list(test_string.split(' '))

new_test_list = [x for x in test_string_list if (x in units) or (x in tens) or (x in scales)]

print(new_test_list)

