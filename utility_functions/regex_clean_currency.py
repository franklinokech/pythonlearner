import re


def clean_currency(s):
    """Function to currency  from string using regex"""
    match = re.findall("([0-9]+[,.]+[0-9]+)", s)
    if len(match) == 2:
        cleaned_salary = "-".join(match).replace(',', '').strip()
    elif len(match) == 1:
        cleaned_salary = match[0].replace(',', '').strip()
    else:
        cleaned_salary = ''

    return cleaned_salary


print(clean_currency('Confidential'))
