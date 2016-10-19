# Pratice 40. Name Sorter
# Input:
#   File name : name_sorter_input
# Output:
#   Total of 7 names
#   ----------------
#   Ling, Mai
#   Johnson, Jim
#   Jones, Aaron
#   Jones, Chris
#   Swift, Geoffrey
#   Xiong, Fong
#   Zarnecki, Sabrina
# Constraint:
#   - Don't hard-code the number of names.

#!/usr/bin/env python

import sys

FILE_NAME = 'name_sorter_input'

def read_file():
    name_list = []

    try:
        with open(FILE_NAME, 'r') as f:
            for line in f.readlines():
                name_list.append(line.strip())
    except:
        print ('File does not exist.')
        exit()

    return name_list

def print_names(in_name_list):
    print ('Total of %s names' % len(name_list))
    print ('------------------')

    for name in in_name_list:
        print (name)

if __name__ == '__main__':
    name_list = read_file()
    name_list.sort()
    print_names(name_list)
