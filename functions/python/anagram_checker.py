# Pratice 24. Anagram checker
# Output:
#   Enter two strings and I'll tell you if they are anagrams:
#   Enter the first string: note
#   Enter the second string: tone
#   "note" and "tone" are anagrams.
# Constraint:
#   - Implement the program using a function called 'isAnagram',
#     which takes in two words as its arguments and returns 'true' or 'false'.
#     Invoke this function from your main program.
#   - Check that both words are the same length.

#!/usr/bin/env python

import sys

def input_process(in_question):
    return input(in_question) if sys.version_info >= (3,0) else raw_input(in_question)

def isAnagram(in_first_str, in_second_str):
    if len(in_first_str) != len(in_second_str):
        return False

    return sorted(in_first_str) == sorted(in_second_str)

if __name__ == '__main__':
    print ('Enter two strings and I\'ll tell you if they are anagrams:')

    first_str = str(input_process('Enter the first string: '))
    second_str = str(input_process('Enter the second string: '))

    result = isAnagram(first_str, second_str)
    if result == True:
        print ('\"%s\" and \"%s\" are anagrams.') % (first_str, second_str)
    else:
        print ('\"%s\" and \"%s\" are not anagrams.') % (first_str, second_str)
