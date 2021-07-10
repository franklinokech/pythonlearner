# import modules
import json
from difflib import get_close_matches

# load data
data = json.load(open('dictionary.json'))
msg_not_found = "The word doesnt exist, please double check"


def translate(w):
    w = w.lower()

    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        closest_word = get_close_matches(w, data.keys())[0]
        yn = input(f'Did you mean {closest_word} instead? Enter Y is yes, or N\n')
        yn = yn.lower()

        if yn == 'y':
            return data[closest_word]
        elif yn == 'n':
            return msg_not_found
        else:
            return msg_not_found
    else:
        return msg_not_found


# driver
word = input("Enter word: \n")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
input('Press Enter to exit')
