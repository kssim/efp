# Pratice 21. Numbers to names
# Output:
#   Please enter the number of the month: 3
#   The name of the month is March.
# Constraint:
#   - Use a switch or case statement for this program.
#   - Use a single output statement for this program.

#!/usr/bin/env python

import sys

def input_process(in_question):
    return input(in_question) if sys.version_info >= (3,0) else raw_input(in_question)

def switch_state(in_option):
    return {
        1 : 'January',
        2 : 'February',
        3 : 'March',
        4 : 'April',
        5 : 'May',
        6 : 'June',
        7 : 'July',
        8 : 'August',
        9 : 'September',
        10 : 'October',
        11 : 'November',
        12 : 'December'
    }.get(in_option)

if __name__ == '__main__':
    try:
        number_month = int(input_process('Please enter the number of the month: '))
    except:
        print ('You must input only numbers.')
    else:
        if number_month < 1 or number_month > 12:
            print ('Wrong input value, you must input number of the month.')
            exit()

        print ('The name of the month is %s.' % switch_state(number_month))
