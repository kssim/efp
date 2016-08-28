# Pratice 1. Saying Hello
# Output:
#   What is your name? Kssim
#   Hello, Kssim, nice to meet you!
# Constraint:
#   - Keep the input, string concatenation, and output separate.

#!/usr/bin/env python

import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ('Please input your name')
        exit(1)

    user_name = sys.argv[1]

    print_str = 'What is your name? '
    print_str += user_name
    print_str += '\n'
    print_str += 'Hello, '
    print_str += user_name
    print_str += ', nice to meet you!'

    print (print_str)
