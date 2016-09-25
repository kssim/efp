# Pratice 26. Months to pay off a credit card
# Output:
#   What is your balance? 5000
#   What is the APR on the card (as a percent)? 12
#   What is the monthly payment you can make? 100
#
#   It will take you 70 months to pay off this card.
# Formula:
#   n = (b + (b * i)) / p
#
#   n is the number of months.
#   i is the daily rate (APR divided by 12[months]).
#   b is the balance.
#   p is the monthly payment.
# Constraint:
#   - Prompt for the card's APR. Do the division internally.
#   - Prompt for the APR as a percentage, not a decimal.
#   - Use a function called 'calculateMonthsUntilPaidOff',
#     which accepts the balance, the APR, and the monthly payment
#     as its arguments and returns the number of months.
#     Don't access any of these values outside the function.
#   - Round fractions of a cent up to the next cent.

#!/usr/bin/env python

import sys

MONTHS = 12

def input_process(in_question):
    return input(in_question) if sys.version_info >= (3,0) else raw_input(in_question)

def calculateMonthsUntilPaidOff(in_balance, in_apr_rate, in_monthly_payment):
    month_rate = 0.4
    apr_per_month = in_apr_rate/MONTHS * month_rate
    months_numbers = (in_balance + (in_balance * apr_per_month)) / in_monthly_payment
    return months_numbers

if __name__ == '__main__':
    try:
        balance = int(input_process('What is your balance? '))
        apr_rate = int(input_process('What is the APR on the card(as a percent)? '))
        monthly_payment = int(input_process('What is the monthly payment you can make? '))
    except:
        print ('You have entered an invalid value.')
    else:
        months_numbers = calculateMonthsUntilPaidOff(balance, apr_rate, monthly_payment)
        print ('It will take you %s months to pay off this card.' % str(months_numbers))
