# Pratice 12. Computing Simple Interest
# Output:
#   Enter the principal: 2000
#   Enter the rate of interest: 5.98
#   Enter the number of years: 3
#   After 3 years at 5.98%, the investment will be worth $2358.8.
# Constraint:
#   - Prompt for the rate as a percentage (like 20%, not 20).
#     Divide the input by 100 in your program.
#   - Ensure that fractions of a cent are rounded up to the next penny.
#   - Ensure that the output is formatted as money.

#!/usr/bin/env python

import sys

def input_process(in_question):
    return input(in_question) if sys.version_info >= (3,0) else raw_input(in_question)


if __name__ == '__main__':
    try:
        principal = int(input_process('Enter the principal: '))
        interest_rate = float(input_process('Enter the rate of interest: '))
        years = int(input_process('Enter the number of years: '))
    except:
        print ('You must input only numbers.')
    else:
        if interest_rate <= 0:
            print ('You must enter a positive number.')
            exit(1)

        interest = round((principal * interest_rate / 100) * years, 2)

        print_str = '''
        After %s years at %s, the investment will be worth %s.
        ''' % (years, interest_rate, (principal + interest))

        print (print_str)
