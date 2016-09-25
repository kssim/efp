# Pratice 31. Karvonen heart rate
# Output:
#   Resting Pulse: 65   Age: 22
#   Intensity   | Rate
#   ------------|----------
#   55%         | 138 bpm
#   60%         | 145 bpm
#   65%         | 151 bpm
#    .          |  .        (extra lines omitted)
#   85%         | 178 bpm
#   90%         | 185 bpm
#   95%         | 191 bpm
# Formular:
#   TargetHeartRate = (((220 - age) - restingHR) x intensity) + restingHR
# Constraint:
#   - Don't hard-code the percentages.
#     Use a loop to increment the percentages from 55 to 95.
#   - Ensure that the heart rate and age are entered as numbers.
#     Don't allow the user to continue without entering valid inputs.
#   - Display the results in a tabular format.

#!/usr/bin/env python

import sys

def input_process(in_question):
    return input(in_question) if sys.version_info >= (3,0) else raw_input(in_question)

def prompt_input():
    try:
        resting_pulse = int(input_process('What is the resting pulse? '))
        age = int(input_process('What is your age? '))
    except:
        print ('You have entered an invalid value.')
        return (-1, -1)
    else:
        return (resting_pulse, age)

if __name__ == '__main__':
    resting_pulse = 0
    age = 0

    while True:
        resting_pulse, age = prompt_input()
        if resting_pulse > 0 and age > 0:
            break

    print ('Resting Pulse: %d   Age: %d' % (resting_pulse, age))
    print ('Intensity   %s Rate' % '|')
    print ('------------%s----------' % '|')

    convert_rate = 220
    for i in range(55, 100, 5):
        target_heart_rate = round((((convert_rate - age) - resting_pulse) * (i*0.01)) + resting_pulse)
        print ('%d%s         %s %d bpm' % (i, '%', '|', target_heart_rate))
