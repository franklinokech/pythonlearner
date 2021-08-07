def display_score(winner, score, **other_info):
    print('The winner is ' + winner)
    print('The score is ' + score)
    for k, v in other_info.items():
        print(k + ': ' + v)


# call
display_score(winner='Chelsea', score='1-0', overtime='Yes', injuries='None', referee='Web')
