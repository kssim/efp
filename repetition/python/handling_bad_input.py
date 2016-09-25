# Pratice 29. Handling bad input
# Output:
#   What is the rate of return? 0
#   Sorry. That's not a valid input.
#   What is the rate of return? ABC
#   Sorry. That's not a valid input.
#   What is the rate of return? 4
#   It will take 18 years to double your initial investment.
# Formula:
#   years = 72 / r
#   - r is the stated rate of return.
# Constraint:
#   - Don't allow the user to enter 0.
#   - Don't allow non-numeric values.
#   - Use a loop to trap bad input, so you can ensure
#     that the user enters valid values.

#!/usr/bin/env python

import sys

def input_process(in_question):
    return input(in_question) if sys.version_info >= (3,0) else raw_input(in_question)

def prompt_input():
    try:
        return_rate = int(input_process('What is the rate of return? '))
        if return_rate <= 0:
            raise Exception()
        return return_rate
    except:
        print ('Sorry. That\'s not a valid input.')
        return -1

if __name__ == '__main__':
    years_formular = 72

    while True:
        return_rate = prompt_input()
        if return_rate != -1:
            print ('It will take %d years to double your initial investment.' % int(years_formular / return_rate))
            break
