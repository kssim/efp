# Pratice 13. Determining Compound Interest
# Output:
#   What is the principal amount? 2000
#   What is the rate: 6.3
#   What is the number of years: 4
#   What is the number of times the interest is compounded per year? 7
#   $2000 invested at 6.3% for 7 years.
#   compounded 4 times per year is $3097.86.
# Formular:
#   A = P(1+r/n)^nt
#
#   A is the amount at the end of the investment.
#   n is the number of times the interest is compunded per year.
#   t is the number of years the amount is invested.
#   r is the annual rate of interest.
#   P is the principal amount.
# Constraint:
#   - Prompt for the rate as a percentage (like 15, not .15).
#     Divide the input by 100 in your program.
#   - Ensure that fractions of a cent are rounded up to the next penny.
#   - Ensure that the output is formatted as money.

#!/usr/bin/env python

import sys

def input_process(in_question):
    return input(in_question) if sys.version_info >= (3,0) else raw_input(in_question)

if __name__ == '__main__':
    try:
        principal = int(input_process('What is the principal amount? '))
        rate = float(input_process('What is the rate? '))
        years = int(input_process('What is the number of years? '))
        interest_years = int(input_process('What is the number of times the interest is compounded per year? '))
    except:
        print ('You must input only numbers.')
    else:
        interest_value = pow((1 + (rate / 100) / years), interest_years * years)
        investment_value = principal * interest_value

        print_str = '''
        $%s invested at %s%s for %s years.
        compounded %s times per year is $%s.
        ''' % (principal, rate, '%', years, interest_years, round(investment_value, 2))

        print (print_str)
