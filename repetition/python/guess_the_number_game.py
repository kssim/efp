# Pratice 32. Guess the number game
# Output:
#   Let's play Guess the Number.
#   Pick a difficulty level (1, 2, or 3): 1
#   I have my number. What's your guess? 1
#   Too low. Guess again: 5
#   Too high. Guess again: 2
#   You got it in 3 guesses!
#   Play again? n
#   Goodbye!
# Constraint:
#   - Don't allow any non-numeric data entry.
#   - During the game, count non-numeric entries as wrong guesses.

#!/usr/bin/env python

import sys
from random import randrange

def input_process(in_question):
    return input(in_question) if sys.version_info >= (3,0) else raw_input(in_question)

def input_int_value(in_str):
    while True:
        try:
            value = int(input_process(in_str))
            if value <= 0:
                raise Exception()
        except:
            print ('You have entered an invalid value.')
        else:
            return value

def set_random_number(in_level):
    if in_level == 1:
        seed_range = 10
    elif in_level == 2:
        seed_range = 100
    else:
        seed_range = 1000

    return randrange(seed_range) + 1

def guess_engine(in_rand_num, in_guess_num):
    guess_num = in_guess_num
    idx = 0

    while True:
        idx += 1;

        if in_rand_num > guess_num:
           guess_num = input_int_value('Too low. Guess again: ')
        elif in_rand_num < guess_num:
           guess_num = input_int_value('Too high. Guess again: ')
        else:
            return idx
def main():
    print ('Let\'s paly Guess the Number.')
    level = 0

    try:
        level = int(input_process('Pick a difficulty level (1, 2, or 3) '))
        if level < 1 or level > 3:
            raise Exception()
    except:
        print ('You have entered an invalid value.')
        exit()

    rand_num = set_random_number(level)
    guess_value = input_int_value('I have my number. What\'s your guess? ')
    idx = guess_engine(rand_num, guess_value)
    print ('You got it in %d guesses!' % idx)

if __name__ == '__main__':
    again = ''

    while again.upper() != 'N':
        main()
        again = str(input_process('Play again? (n or any input) '))

    print ('Goodbye!')
