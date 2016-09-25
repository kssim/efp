# Pratice 28. Adding numbers
# Output:
#   Enter a number: 1
#   Enter a number: 2
#   Enter a number: 3
#   Enter a number: 4
#   Enter a number: 5
#   The total is 15.
# Constraint:
#   - The prompting must use repetition, such as a counted loop,
#     not three separate prompts.
#   - Create a flowchart before writing the program.

#!/usr/bin/env python

import sys

def input_process(in_question):
    return input(in_question) if sys.version_info >= (3,0) else raw_input(in_question)

def prompt_number():
    try:
        return int(input_process('Enter a number: '))
    except:
        print ('You have entered an invalid value.')
        print ('This value is skipped.')
        return 0

if __name__ == '__main__':
    total_value = 0

    for i in range(5):
        total_value += prompt_number()

    print ('The total is %d' %  total_value)
