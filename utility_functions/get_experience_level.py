import re


# utilities
def parse_int(textnum, numwords={}):
    """
    Function return a number representation of a numeric given in words e.g three->3
    :param textnum: text representing number
    :param numwords: dictionary of number and words
    :return: a number representing text given
    """
    textnum = textnum.lower()

    textnum = textnum.split(' ')

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

    textnum = [x for x in textnum if (x in units) or (x in tens) or (x in scales)]
    # create our default word-lists
    if not numwords:

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

        # divisors
        numwords["and"] = (1, 0)

        # perform our loops and start the swap
        for idx, word in enumerate(units):    numwords[word] = (1, idx)
        for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    # primary loop
    current = result = 0
    # loop while splitting to break into individual words

    # remove non numbers words

    for word in textnum:
        # if problem then fail-safe
        if word not in numwords:
            raise Exception("Illegal word: " + word)

        # use the index by the multiplier
        scale, increment = numwords[word]
        current = current * scale + increment

        # if larger than 100 then push for a round 2
        if scale > 100:
            result += current
            current = 0

    # return the result plus the current
    return result + current


def get_year_experience(experience_string):
    """
    This function given a experience string return the minimum experience needed in Years
    :param experience_string: experience string from scrapped data
    :return: min experience level in Years
    """
    min_experience = ''
    experience_string = experience_string.strip().lower()

    if 'year' in experience_string:
        years_range = re.findall(r'\d+', experience_string)
        if len(years_range) >= 1:
            min_experience = int(years_range[0])

        elif len(years_range) == 0:
            min_experience = parse_int(experience_string)

    elif 'month' in experience_string:
        month_range = re.findall(r'\d+', experience_string)
        if len(month_range) >= 1:
            min_experience = int(month_range[0]) / 12

        elif len(month_range) == 0:
            min_experience = parse_int(experience_string) / 12

    return min_experience


print(get_year_experience('five years'))
