# Pratice 9. Pain Calculator
# Output:
#   You will need to purchase 2 liters of paint
#   to cover 10 square meter.
# Formula :
#   1 liter covers 9 square meter
# Constraint:
#   - Use a constant to hold the conversion rate.
#   - Ensure that you round up to the next whole number.

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
        cover_meter = 9
        room_square_meter = room_length * width_length

        if room_square_meter % cover_meter != 0:
            required_liter = int(room_square_meter / cover_meter) + 1
        else:
            required_liter = int(room_square_meter / cover_meter)

        print_str = 'You will need to purchase %s liters of paint to cover %s square meter.' % (required_liter, room_square_meter)
        print (print_str)
