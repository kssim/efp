# Pratice 23. Troubleshooting car issues.
# Output:
#   Is the car silent when you turn the key? y
#   Are the battery terminals corroded? n
#   Replace cables and try again.
# Constraint:
#   - Ask only questions that are relevant to the situation and
#     to the previous answers. Don't ask for all inputs at once.

#!/usr/bin/env python

import sys

def input_process(in_question):
    return input(in_question) if sys.version_info >= (3,0) else raw_input(in_question)

if __name__ == '__main__':
    answer = str(input_process('Is the car silent when you turn the key? '))
    if answer.upper() == 'Y':
        answer = str(input_process('Are the battery terminals corroded? '))
        if answer.upper() == 'Y':
            print ('Clean terminals and try starting again.')
            exit()
        elif answer.upper() == 'N':
            print ('Replace cables and try again.')
            exit()
    elif answer.upper() == 'N':
        answer = str(input_process('Does the car make a clicking noise? '))
        if answer.upper() == 'Y':
            print ('Replace the battery.')
            exit()
        elif answer.upper() == 'N':
            answer = str(input_process('Does the car crank up but fail to start? '))
            if answer.upper() == 'Y':
                print ('Check spark plug connections.')
                exit()
            elif answer.upper() == 'N':
                answer = str(input_process('Does the engine start and then die? '))
                if answer.upper() == 'Y':
                    answer = str(input_process('Does your car have fuel injection? '))
                    if answer.upper() == 'Y':
                        print ('Get it in for service.')
                        exit()
                    elif answer.upper() == 'N':
                        print ('Check to ensure the choke is opening and closing.')
                        exit()

    print ('You input wrong value.')
