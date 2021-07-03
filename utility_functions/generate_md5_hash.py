import hashlib


def get_hash_value(my_string):
    """

    :param my_string: string to be hashed
    :return: md5 hash of the string
    """
    result = hashlib.md5(my_string.encode())
    my_hash = result.hexdigest()

    return my_hash
