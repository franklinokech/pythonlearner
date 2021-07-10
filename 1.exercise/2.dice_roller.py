import random


def roll_dice():
    print('You rolled ', random.randint(1, 6))


while True:
    user_choice = int(input('Do you want to roll a dice? enter 1 to continue, 0 to quit\n'))
    if user_choice == 0:
        print('Thank you for using Frank Dice')
        break

    elif user_choice == 1:
        roll_dice()
