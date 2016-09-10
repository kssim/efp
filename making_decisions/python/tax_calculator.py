# Pratice 14. Tex-Calculator
# Output:
#   What is the order amount? 10
#   What is the state? WI
#   The subtotal is $10.00
#   The tax is $0.55
#   The total is $10.55
#   Or
#   What is the order amount? 10
#   What is the state? MN
#   The subtotal is $10.55
# Constraint:
#   - Implement this program using only a simple if state-ment-don't use an 'else' clause.
#   - Ensure that all money is rounded up to the nearest cent.
#   - Use a single output statement at the end of the program to display the program result.

#!/usr/bin/env python

import sys

def input_process(in_question):
    return input(in_question) if sys.version_info >= (3,0) else raw_input(in_question)


if __name__ == '__main__':
    try:
        order_amount = int(input_process('What is the order amount? '))
        state = str(input_process('What is the state? '))
    except:
        print ('You must input only numbers.')
    else:
        print_str = ''
        tax = 0
        tax_rate = 0.055
        tax = round(order_amount * tax_rate, 2)

        if state.upper() == 'WI':
            print_str = '''
            The subtotal is $%s
            The tax is $%s
            The total is $%s
            ''' % (order_amount, tax, order_amount + tax)

        if state.upper() != 'WI':
            print_str = '''
            The total is $%s
            ''' % (order_amount + tax)

        print (print_str)
