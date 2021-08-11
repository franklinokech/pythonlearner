import re


def clean_currency(s):
    """
    Function takes in string containing salary data and returns salary in numericals
    :param s: salary string
    :return: cleaned salary containing numericals only
    """
    s = s.replace(',', '').replace(' ', '')

    match = re.findall("[0-9]+", s)

    if len(match) == 2:
        # find average
        cleaned_salary = (int(match[0]) + int(match[1])) / 2
    elif len(match) == 1:
        cleaned_salary = int(match[0])

    else:
        cleaned_salary = ''

    return cleaned_salary


print(clean_currency('$10000-14000'))
