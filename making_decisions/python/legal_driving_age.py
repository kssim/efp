# Pratice 16. Legal driving age
# Output:
#   What is your age? 13
#   You are not old enough to legally drive.
#   Or
#   What is your age? 25
#   You are old enough to legally drive.
# Standard:
#   20 years old.
# Constraint:
#   - Use a single output statement.
#   - Use a ternary operator to write this program.
#     If your language doesn't support a ternary operator,
#     use a regular 'if/else' statement, and still use a single output
#     statement to display the message.

#!/usr/bin/env python

import sys

def input_process(in_question):
    return input(in_question) if sys.version_info >= (3,0) else raw_input(in_question)


if __name__ == '__main__':
    try:
        age = int(input_process('What is your age? '))
    except:
        print ('You must input only numbers.')
    else:
        print_str = 'You are old enough to legally drive' if age >= 20 else 'You are not old enough to legally drive'
        print (print_str)
