# Pratice 20. Multistate sales tax calculator
# Output:
#   What is the order amount? 10
#   What state do you live in? Wisconsin
#   What county do you live in? Eau Claire
#   The state tax is $0.55.
#   The county tax is $0.05.
#   The total tax is $0.60.
#   The total is $10.60.
#   Or
#   What is the order amount? 10
#   What state do you live in? Illinois
#   The total tax is $0.80.
#   The total is $10.80.
# Standard:
#   State
#   Illinois : 0.08
#   County (If state is Wisconsin)
#       - Eau Claire : 0.005
#       - Dunn : 0.004
# Constraint:
#   - Ensure that all money is rounded up to the nearest cent.
#   - Use a single output statement at the end of the program to display the program results.

#!/usr/bin/env python

import sys

def input_process(in_question):
    return input(in_question) if sys.version_info >= (3,0) else raw_input(in_question)


if __name__ == '__main__':
    try:
        amount = int(input_process('What is the order amount? '))
        state = str(input_process('What state do you live in? '))

        exists_county = False
        if state.upper() == 'WISCONSIN':
            county = str(input_process('What county do you live in? '))
            exists_county = True
    except:
        print ('You must input only numbers.')
    else:
        county_tax = 0

        if state.upper() == 'WISCONSIN':
            if county.replace(' ','').upper() == 'EAUCLAIRE':
                county_tax = amount * 0.005
            elif county.replace(' ','').upper() == 'DUNN':
                county_tax = amount * 0.004
            else:
                county_tax = 0
            tax = amount * 0.055
        elif state.upper() == 'ILLINOIS':
            tax = amount * 0.08
        else:
            tax = 0

        print_str = 'The state tax is $%s\n' % round(tax, 2)

        if exists_county == True:
            print_str += 'The county tax is $%s\n' % round(county_tax, 2)

        print_str += 'The total tax is $%s\n' % round((tax + county_tax), 2)
        print_str += 'The total is $%s' % round((amount + tax + county_tax), 2)

        print (print_str)
