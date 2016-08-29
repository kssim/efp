# Pratice 8. Pizza Party
# Output:
#   How many people? 22
#   How many pizzas do you have? 3
#   22 people with 3 pizzas
#   Each person gets 1 pieces of pizza.
#   There are 2 leftover pieces.

#!/usr/bin/env python

import sys

def input_process(in_question):
    return input(in_question) if sys.version_info >= (3,0) else raw_input(in_question)


if __name__ == '__main__':
    try:
        people_num = int(input_process('How many people? '))
        pizzas_num = int(input_process('How many pizzas do you have? '))
    except:
        print ('You must input only numbers.')
    else:
        pizza_pieces_num = (pizzas_num * 8)
        print_str = '''
        %s people with %s pizzas
        Each person gets %s pieces of pizza.
        There are %s leftover pieces.
        ''' % (people_num, pizzas_num, int(pizza_pieces_num / people_num), int(pizza_pieces_num % people_num))

        print (print_str)
