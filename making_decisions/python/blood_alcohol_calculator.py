# Pratice 17. Blood alcohol calculator
# Output:
#   Your BAC is 0.08
#   It is not legal for you to drive.
# Formula:
#   BAC = (A x 5.14/W x r)-.015 x H
#   A is total alcohol consumed, in ounces(oz).
#   W is body weight in pounds.
#   r is the alcohol distribution ratio:
#       - 0.73 for men
#       - 0.66 for women
#   H is number of hours since the last drink.
# Standard:
#   BAC = 0.08 under.
# Constraint:
#   - Prevent the user from entering non-numeric values.

#!/usr/bin/env python

import sys

def input_process(in_question):
    return input(in_question) if sys.version_info >= (3,0) else raw_input(in_question)


if __name__ == '__main__':
    try:
        weight = int(input_process('What is your weight? '))
        gender = str(input_process('What is your gender(m or f)? '))
        total_alcohol = int(input_process('How much do you drink alcohol(oz)? '))
        last_drink_time = int(input_process('What is number of hours since the last drink? '))
    except:
        print ('You must input only numbers.')
    else:
        if gender.upper() != 'M' and gender.upper() != 'F':
            print ('You must input \'M\' or \'F\'.')
            exit()

        male_alcohol_ratio = 0.73
        female_alcohol_ratio = 0.66
        oz_calculation_value = 5.14
        last_drink_time_calculation_value = .015
        legal_standard_bac = 0.08

        alcohol_ratio = male_alcohol_ratio if gender.upper() == 'M' else female_alcohol_ratio
        bac_value = (total_alcohol * oz_calculation_value / weight * alcohol_ratio) - (last_drink_time_calculation_value * last_drink_time)

        print ('Your BAC is %s' % bac_value)

        if bac_value < legal_standard_bac:
            print ('It is legal for you to drive.')
        else:
            print ('It is not legal for you to drive.')
