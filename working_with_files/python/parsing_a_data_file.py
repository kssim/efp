# Pratice 41. Parsing a Data File
# Input:
#   File name : parsing_a_data_file_input
# Output:
#   Last     First    Salary
#   ------------------------
#   Ling     Mai      55900
#   Johnson  Jim      56500
#   Jones    Aaron    46000
#   Jones    Chris    34500
#   Swift    Geoffrey 14200
#   Xiong    Fong     65000
#   Zarnecki Sabrina  51500
# Constraint:
#   - Write your own code to parse the data.
#     Don'y use a CSV parser.
#   - Use spaces to align the columns.
#   - Make each column one space longer than the longest value in the column.

#!/usr/bin/env python

import sys

FILE_NAME = 'parsing_a_data_file_input'

LAST_NAME_IDX    = 0
FIRST_NAME_IDX   = 1
SALARY_IDX       = 2

def read_file():
    data_list = []

    try:
        with open(FILE_NAME, 'r') as f:
            for line in f.readlines():
                data_list.append(line.strip().split(','))
    except:
        print ('File does not exist.')
        exit()

    return data_list

def get_data_length(in_data_list):
    last_name_len = 0
    first_name_len = 0
    salary_len = 0

    for data in in_data_list:
        last_name_len = last_name_len if last_name_len > len(data[LAST_NAME_IDX]) else len(data[LAST_NAME_IDX])
        first_name_len = first_name_len if first_name_len > len(data[FIRST_NAME_IDX]) else len(data[FIRST_NAME_IDX])
        salary_len = salary_len if salary_len > len(data[SALARY_IDX]) else len(data[SALARY_IDX])

    return (last_name_len + 1, first_name_len + 1, salary_len + 1)

def print_names(in_data_list):
    (last_name_len, first_name_len, salary_len) = get_data_length(in_data_list)

    print('{:' '<{}}{:' '<{}}{:' '<{}}'.format('Last', last_name_len, 'First', first_name_len, 'Salary', salary_len))
    print ('-------------------------')

    for data in in_data_list:
        print('{:' '<{}}{:' '<{}}{:' '<{}}'.format(data[LAST_NAME_IDX], last_name_len, \
                    data[FIRST_NAME_IDX], first_name_len, data[SALARY_IDX], salary_len))

if __name__ == '__main__':
    data_list = read_file()
    print_names(data_list)
