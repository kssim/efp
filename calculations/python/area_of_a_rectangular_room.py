# Pratice 7. Area of a Rectangular Room
# Output:
#   What is the length of the room in feet? 30
#   What is the width of the room in feet? 20
#   You entered dimensions of 30 feet by 20 feet.
#   The area is 600 square feet
#   55.741824 square meters
# Formula:
#   m^2 = f^2 x 0.09290304
# Constraint:
#   - Keep the calculations separate from the output.
#   - Use a constant to hold the conversion factor.

#!/usr/bin/env python

import sys

def input_process(in_question):
    return input(in_question) if sys.version_info >= (3,0) else raw_input(in_question)


if __name__ == '__main__':
    try:
        room_length = int(input_process('What is the length of the room in feet? '))
        width_length = int(input_process('What is the width of the room in feet? '))
    except:
        print ('You must input only numbers.')
    else:
        conversion_factor = 0.09290304
        square_feet = room_length * width_length

        print_str = '''
        You entered dimensions of %s feet by %s feet.
        The area is %s square feet
        %s square meters
        ''' % (room_length, width_length, square_feet, (square_feet * conversion_factor))

        print (print_str)
