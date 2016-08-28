# Pratice 5. Simple Math
# Output:
#   What is the first number? 20
#   What is the second number? 5
#   20 + 5 = 25
#   20 - 5 = 15
#   20 * 5 = 100
#   20 / 5 = 4
# Constraint:
#   - Values coming from users will be strings. Ensure that you
#     convert these values to numbers before doing the math.
#   - Keep the inputs and outputs separate from the numerical
#     conversions and other processing.
#   - Generate a single output statement with line breaks in the
#     appropriate spots.

#!/usr/bin/env python

import sys

def input_process(in_question):
    return input(in_question) if sys.version_info >= (3,0) else raw_input(in_question)


if __name__ == '__main__':
    first_num_str = input_process('What is the first number? ')
    second_num_str = input_process('What is the second number? ')

    try:
        first_num = int(first_num_str)
        second_num = int(second_num_str)
    except:
        print ('You must input only numbers.')
    else:
        print_str = '%s + %s = %s' % (first_num, second_num, first_num + second_num)
        print_str += '\n'
        print_str += '%s = %s = %s' % (first_num, second_num, first_num - second_num)
        print_str += '\n'
        print_str += '%s * %s = %s' % (first_num, second_num, first_num * second_num)
        print_str += '\n'
        print_str += '%s / %s = %s' % (first_num, second_num, first_num / second_num)

        print (print_str)
