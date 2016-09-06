# Pratice 10. Self-Checkout
# Output:
#   Enter the price of item 1: 25
#   Enter the quantity of item 1: 2
#   Enter the price of item 2: 10
#   Enter the quantity of item 2: 1
#   Enter the price of item 3: 4
#   Enter the quantity of item 3: 1
#   Subtotal: $64.00
#   Tax: $3.52
#   Total: $67.52
# Constraint:
#   - Keep the input, processing, and output parts of your program separate.
#     Collect the input, then do the math operations and string building,
#     and then print out the output.
#   - Be sure you explicitly convert input to numerical data before doing
#     any calculations.

#!/usr/bin/env python

import sys
from datetime import datetime

def input_process(in_question):
    return input(in_question) if sys.version_info >= (3,0) else raw_input(in_question)


if __name__ == '__main__':
    item_list = []

    try:
        for i in range(3):
            item_price = int(input_process('Enter the price of item %s: ' % (i+1) ))
            item_count = int(input_process('Enter the quantity of item %s: ' % (i+1) ))
            item_list.append((item_price, item_count))
    except:
        print ('You must input only numbers.')
    else:
        subtotal = 0
        tax_rate = 5.5

        for item in item_list:
            subtotal += (item[0] * item[1])

        tax = round(subtotal * tax_rate / 100, 2)
        total = round(subtotal + tax, 2)

        print_str = '''
        Subtotal: $%s
        Tax: $%s
        Total: $%s
        ''' % (subtotal, tax, total)

        print (print_str)
