# Pratice 4. Mad Lib
# Output:
#   Enter a noun: cat
#   Enter a verb: beleive
#   Enter an adjective: adorable
#   Enter an adverb: seriously
#   Do you beleive your adorable cat seriously?
# Constraint:
#   - Use a single output statement for this program.
#   - If your language supports string interpolation or string
#     substitution, use it to build up the output.

#!/usr/bin/env python

import sys

def input_process(in_question):
    return input(in_question) if sys.version_info >= (3,0) else raw_input(in_question)


if __name__ == '__main__':
    noun = input_process('Enter a noun: ')
    verb = input_process('Enter a verb: ')
    adjective = input_process('Enter a adjective: ')
    adverb = input_process('Enter a adverb: ')

    print ('Do you %s your %s %s %s?' % (verb, adjective, noun, adverb))
