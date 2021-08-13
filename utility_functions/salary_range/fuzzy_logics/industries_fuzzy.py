from fuzzywuzzy import process

with open('industries.txt', 'r') as f:
    industries = f.read().split('\n')


def get_matches(query, choices, limit=3):
    """
    Function takes in a query, choice and limit do a fuzzy logic and return matching results
    :param query: string to be searched
    :param choices: list of possible choices
    :return: closest match
    """
    results = process.extractOne(query, choices)
    return results


print(get_matches('Non-profit, social work', industries)[0])
