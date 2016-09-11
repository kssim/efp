# Pratice 18. Temperature converter
# Output:
#   Press C to convert from Fahrenheit to Celsius.
#   Press F to convert from Celsius to Fahrenheit.
#   Your choice: C
#
#   Please enter the temperature in Fahrenheit: 32
#   The temperature in Celsius is 0.
# Formula:
#   C = (F - 32) x 5/9
#   F = (C x 9/5) + 32
# Constraint:
#   - Ensure that you allow upper or lowercase values for C and F.
#   - Use as few output statements as possible and avoid repeating output strings.

#!/usr/bin/env python

import sys

def input_process(in_question):
    return input(in_question) if sys.version_info >= (3,0) else raw_input(in_question)


if __name__ == '__main__':
    print ('Press C to convert from Fahrenheit to Celsius.')
    print ('Press F to convert from Celsius to Fahrenheit.')

    try:
        convert_type = str(input_process('Your choice: '))
        temperature = int(input_process('Please enter the temperature in Fahrenheit: '))
    except:
        print ('You must input only numbers.')
    else:
        if convert_type.upper() != 'C' and convert_type.upper() != 'F':
            print ('You must input \'C\' or \'F\'.')
            exit()

        convert_value = 32

        if convert_type.upper() == 'C':
            convert_temperature = (temperature - convert_value) * (5/9)
        elif convert_type.upper() == 'F':
            convert_temperature = (temperature * (9/5)) + convert_value

        print ('The temperature in Celsius is %s.' % convert_temperature)
