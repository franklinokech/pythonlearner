import re


def extract_email(s):
    """Function to extract email address from string using regex"""
    lst = re.findall('\S+@\S+', s)

    return lst
