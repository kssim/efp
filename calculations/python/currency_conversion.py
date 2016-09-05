# Pratice 11. Currency Conversion
# Output:
#   How many euros are you exchanging? 81
#   What is the exchange rate? 134.81
#   81 euros at an exchange rate of 134.81
#   109.20 U.S. dollars.
# Constraint:
#   - Ensure that fractions of a cent are rounded up to the next penny.
#   - Use a single output statement.

#!/usr/bin/env python

import sys

def input_process(in_question):
    return input(in_question) if sys.version_info >= (3,0) else raw_input(in_question)


if __name__ == '__main__':
    try:
        euros = int(input_process('How many euros are you exchanging? '))
        exchange_rate = float(input_process('What is the exchange rate? '))
    except:
        print ('You must input only numbers.')
    else:
        if euros <= 0:
            print ('You must enter a positive number.')
            exit(1)

        dollars = round((euros * exchange_rate / 100), 2)

        print_str = '''
        %s euros at an exchange rate of %s
        %s U.S. dollars.
        ''' % (euros, exchange_rate, dollars)

        print (print_str)
