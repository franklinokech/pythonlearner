def remove_bad_substrings(s):
    """
    Remove a bad string from a string
    :param s: The string containing bad strings
    :return: a formated strip with bad strings removed
    """
    bad_strings = ['KSh', 'ksh']
    for badSubstring in bad_strings:
        s = s.replace(badSubstring, "").strip()
    return s


# Test
print(remove_bad_substrings('KSh 300,000 - 400,000'))
