# Pratice 15. Password validation
# Output:
#   What is the username: kssim
#   What is the password: 12345
#   I don't know you.
#   Or
#   What is the username: kssim
#   What is the password: abc$123
#   Welcome!
# Constraint:
#   - Use an 'if/else' statement for this problem.
#   - Make sure the program is case sensitive.

#!/usr/bin/env python

import sys

def input_process(in_question):
    return input(in_question) if sys.version_info >= (3,0) else raw_input(in_question)


if __name__ == '__main__':
    try:
        username = str(input_process('What is the username? '))
        password = str(input_process('What is the password? '))
    except:
        print ('You have entered an invalid value.')
    else:
        if username == 'kssim' and password == 'abc$123':
            print ('Welcome!')
        else:
            print ('I don\'t know you.')
