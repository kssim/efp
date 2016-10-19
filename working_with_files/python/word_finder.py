# Pratice 45. Word Finder
# Output:
#   Given the input file of
#   'One should never utilize the word "utilize" in writing. Use "use" instead.'
#   The program should generate
#   'One should never use the word "use" in writing. Use "use" instead.'
# Constraint:
#   - Prompt for the name of the output file.
#   - Write the output to a new file.

#!/usr/bin/env python

import sys

FILE_NAME = 'word_finder_input'

def input_process(in_question):
    return input(in_question) if sys.version_info >= (3,0) else raw_input(in_question)

def get_file_data():
    try:
        with open(FILE_NAME, 'r') as f:
            return f.read()
    except:
        print ('File does not created.')
        exit()

    return ''

def write_replace_file(in_input_file_name, in_data):
    try:
        with open(in_input_file_name, 'w') as f:
            f.write(in_data.replace('utilize', 'use'))
    except:
        print ('File was not created.')
        exit()

if __name__ == '__main__':
    input_file_name = str(input_process('Input your file name : '))
    data = get_file_data()
    write_replace_file(input_file_name, data)
