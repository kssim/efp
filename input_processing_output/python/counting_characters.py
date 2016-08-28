# Pratice 2. Counting the Number of Characters
# Output:
#   What is the input string? kssim
#   kssim has 5 characters.
# Constraints:
#   - Be sure the output contains the original string.
#   - Use a single output statement to construct the output.
#   - Use a built-in function of the programming language to
#     determine the length of the string.

#!/usr/bin/env python

import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ('Please input string.')
        exit(1)

    input_str = sys.argv[1]

    print_str = 'What is the input string? '
    print_str += input_str
    print_str += '\n'
    print_str += input_str
    print_str += ' has '
    print_str += str(len(input_str))
    print_str += ' characters.'

    print (print_str)
