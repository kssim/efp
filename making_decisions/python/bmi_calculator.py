# Pratice 19. BMI Calculator
# Output:
#   Your BMI is 19.5.
#   You are within the ideal weight range.
#   Or
#   Your BMI is 32.5.
#   You are overweight. You should see your doctor.
# Formula:
#   bmi = (weight / (height x height)) x 703
# Standard:
#   BMI 18.5 ~ 25 is nomal weight.
# Constraint:
#   - Ensure your program takes only numeric data.
#     Don't let the user continue unless the data is valid.

#!/usr/bin/env python

from __future__ import division
import sys

def input_process(in_question):
    return input(in_question) if sys.version_info >= (3,0) else raw_input(in_question)


if __name__ == '__main__':
    try:
        weight = int(input_process('What is your weight(pound)? '))
        height = int(input_process('What is your height(inch)? '))
    except:
        print ('You must input only numbers.')
    else:
        bmi_convert_value = 703
        bmi_raw_data = float(weight / (height * height))
        bmi = bmi_raw_data * bmi_convert_value

        print ('Your BMI is %s' % bmi)

        if bmi < 18.5:
            print ('You are within the ideal weight range.')
        elif bmi > 25:
            print ('You are overweight. You should see your doctor.')
        else:
            print ('You are nomal weight.')
