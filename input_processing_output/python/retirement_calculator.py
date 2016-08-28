# Pratice 6. Retirement Calculator
# Output:
#   What is your current age? 27
#   At what age would you like to retire? 70
#   You have 43 years left until you can retire.
#   It's 2016, so you can retire in 2059.
# Constraint:
#   - Agian, be sure to convert the input to numerical data
#     before doing any math.
#   - Don't hard-code the current year into your program.
#     Get it from the system time via your programming language.

#!/usr/bin/env python

import sys
from datetime import datetime

def input_process(in_question):
    return input(in_question) if sys.version_info >= (3,0) else raw_input(in_question)


if __name__ == '__main__':
    current_age_str = input_process('What is your current age? ')
    retire_age_str = input_process('At what age would you like to retire? ')

    try:
        current_age = int(current_age_str)
        retire_age = int(retire_age_str)
    except:
        print ('You must input only numbers.')
    else:
        if current_age >= retire_age:
            print('You must input retire age lagger than current age.')
            exit(1)

        left_year = retire_age - current_age
        current_year = datetime.today().year

        print_str = 'You have %s years left until you can retire.' % (left_year)
        print_str += '\n'
        print_str += 'It\'s %s, so you can retire in %s.' % (current_year, current_year + left_year)

        print (print_str)
