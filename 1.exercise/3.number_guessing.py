"""
The Algorithm:
    User inputs the lower bound and upper bound of the range.
    The compiler generates a random integer between the range and store it in a variable for future references.
    For repetitive guessing, a while loop will be initialized.
    If the user guessed a number which is greater than a randomly selected number, the user gets an output “Try Again! You guessed too high“
    Else If the user guessed a number which is smaller than a randomly selected number, the user gets an output “Try Again! You guessed too small”
    And if the user guessed in a minimum number of guesses, the user gets a “Congratulations! ” Output.
    Else if the user didn’t guess the integer in the minimum number of guesses, he/she will get “Better Luck Next Time!” output.
"""

import random
import math

# user inputs
lower_bound = int(input('Enter the Lower Bound\n'))
upper_bound = int(input('Enter the Upper Bound\n'))

# Generate a random number between
generated_number = random.randint(lower_bound, upper_bound)

print("\n\tYou've only ", round(math.log(upper_bound - lower_bound + 1, 2)), " chances to guess the integer!\n")

# initialise number of guesses
count = 0
while count < math.log(upper_bound - lower_bound + 1, 2):
    count += 1
    # guess
    guess = int(input('Guess a number\n'))

    # condition testing
    if generated_number == guess:
        print(f'Congratulation, you guessed correct in {count} try')
        break
    elif generated_number > guess:
        print('You guessed too small!')
    elif generated_number < guess:
        print('You guessed too high')

# once exhausted number of guessed, show the number
if count > math.log(upper_bound-lower_bound+1, 2):
    print(f'The number is {generated_number} Good luck next time')
