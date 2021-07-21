# file with word:meaning,
import json
from difflib import get_close_matches

# Load the json
data = json.load(open('dictionary.json'))
msg_not_found = 'The Word is not available'


def translate(w):
    w = w.lower()

    if w in data:
        return data[w]

    elif len(get_close_matches(w, data.keys())) > 0:
        closest_match = data[get_close_matches(w, data.keys())][0]
        yn = input(f'Did you mean {closest_match} , enter Y, or N')
        yn = yn.lower()

        if yn == 'y':
            return data[closest_match]
        elif yn == 'n':
            return msg_not_found
    else:
        return msg_not_found