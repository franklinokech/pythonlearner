def parse_int(textnum, numwords={}):
    textnum = textnum.lower()

    textnum = textnum.split(' ')
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

    textnum = [x for x in textnum if (x in units) or (x in tens) or (x in scales)]

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


print(parse_int('thirty six months'))