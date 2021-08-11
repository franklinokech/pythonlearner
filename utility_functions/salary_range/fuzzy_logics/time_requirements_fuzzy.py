from fuzzywuzzy import process

with open('time_requirements.txt', 'r') as f:
    time_requirements = f.read().split('\n')


def get_matches(query, choices, limit=3):
    """
    Function takes in a query, choice and limit do a fuzzy logic and return matching results
    :param query: string to be searched
    :param choices: list of possible choices
    :param limit: return match limit
    :return: list of matches
    """
    results = process.extract(query, choices, limit=limit)
    return results


print(get_matches('Contract', time_requirements, limit=3))
