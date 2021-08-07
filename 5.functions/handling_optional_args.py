def display_winner(winner, score, **other):
    print('The winner is ' + winner)
    print('The score was ' + score)
    for k, v in other.items():
        print(k + ': ' + v)


display_winner(winner='Chelsea', score='1-0', redcard='2')
