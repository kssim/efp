# Pratice 22. Comparing numbers
# Output:
#   Enter the first number: 1
#   Enter the second number: 51
#   Enter the third number: 2
#   The largest number is 51.
# Constraint:
#   - Write the algorithm manually.
#     Don't use a built-in function for finding the largest number in a list.

#!/usr/bin/env python

import sys

def input_process(in_question):
    return input(in_question) if sys.version_info >= (3,0) else raw_input(in_question)

if __name__ == '__main__':
    try:
        number_one = int(input_process('Enter the first number: '))
        number_two = int(input_process('Enter the second number: '))
        number_three = int(input_process('Enter the third number: '))
    except:
        print ('You must input only numbers.')
    else:
        if number_one == number_two or number_one == number_three or number_two == number_three:
            print ('You input the same number.')
            exit()

        largest_number = number_one if number_one > number_two else number_two
        largest_number = largest_number if largest_number > number_three else number_three

        print ('The largest number is %s.' % largest_number)
