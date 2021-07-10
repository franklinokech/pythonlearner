import secrets
import string
import random


def generate_password(password_len):
    """
    this function generates a password of a given lenght
    :param password_len: int lenght of password
    :return: str secure password
    """
    password = ''

    for x in range(0, 4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(
            string.digits) + random.choice(string.punctuation)
    for y in range(password_len - 4):
        password = password + random.choice(
            string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    return password
