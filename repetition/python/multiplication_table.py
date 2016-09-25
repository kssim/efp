# Pratice 30. Multiplication table
# Output:
#   0 x 0 = 0
#   0 x 1 = 0
#   12 x 11 = 132
#   12 x 12 = 144
# Constraint:
#   - Use a nested loop to complete this program.

#!/usr/bin/env python

import sys

def input_process(in_question):
    return input(in_question) if sys.version_info >= (3,0) else raw_input(in_question)

if __name__ == '__main__':
    FIXED_LOOP_NUM = 13

    for i in range(FIXED_LOOP_NUM):
        for j in range(FIXED_LOOP_NUM):
            print ('%d x %d = %d' % (i, j, i*j))
