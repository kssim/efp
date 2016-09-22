# Pratice 27. Validating inputs
# Output:
#   Enter the first name: J
#   Enter the last name:
#   Enter the ZIP code : ABCDE
#   Enter an employee ID : A12-1234
#   "J" is not a valid first name. It is too short.
#   The last name must be filled in.
#   The ZIP code must be numeric.
#   A12-1234 is not a valid ID.
#   Or
#   Enter the first name: Jimmy
#   Enter the last name: James
#   Enter the ZIP code : 5555
#   Enter an employee ID : TK-421
#   There were no errors found.
# Rule:
#   The first name must be filled in.
#   The last name must be filled in.
#   The first and last names must be at least two characters long.
#   An employee ID is in the format AA-1234, So, two letters, a hyphen, and four numbers.
#   The ZIP code must be a number.
# Constraint:
#   - Create a function for each type of validation you need to write.
#     Then create a 'validateInput' function that takes in all of
#     the input data and invokes the specific validation functions.
#   - Use a single output statement to display the outputs.

#!/usr/bin/env python

import sys
from re import match

UNDER_LIMIT_NAME_COUNT = 2

def input_process(in_question):
    return input(in_question) if sys.version_info >= (3,0) else raw_input(in_question)

def check_first_name(in_first_name):
    err_str = ''

    if len(in_first_name.strip()) == 0:
        err_str = 'The first name must be filled in.\n'
        return (False, err_str)

    if len(in_first_name.strip()) < UNDER_LIMIT_NAME_COUNT:
        err_str = '\"%s\" is not a valid first name. It is too short.\n' % in_first_name
        return (False, err_str)

    return (True, '')

def check_last_name(in_last_name):
    err_str = ''

    if len(in_last_name.strip()) == 0:
        err_str = 'The last name must be filled in.\n'
        return (False, err_str)

    if len(in_last_name.strip()) < UNDER_LIMIT_NAME_COUNT:
        err_str = '\"%s\" is not a valid last name. It is too short.\n' % in_last_name
        return (False, err_str)

    return (True, '')

def check_zip_code(in_zip_code):
    try:
        zip_code = int(in_zip_code)
    except:
        err_str = 'The ZIP code must be numeric.\n'
        return (False, err_str)
    return (True, '')

def check_employee_id(in_employee_id):
    if bool(match('^[a-zA-Z]{2}-[\d]{4}$', in_employee_id)) == False:
        err_str = '%s is not a valid ID.\n' % in_employee_id
        return (False, err_str)
    return (True, '')

def validateInput(in_first_name, in_last_name, in_zip_code, in_employee_id):
    err_str = ''

    return (check_first_name(in_first_name), \
            check_last_name(in_last_name), \
            check_zip_code(in_zip_code), \
            check_employee_id(in_employee_id))

if __name__ == '__main__':
    first_name = str(input_process('Enter the first name: '))
    last_name = str(input_process('Enter the last name: '))
    zip_code = str(input_process('Enter the ZIP code: '))
    employee_id = str(input_process('Enter an employee ID: '))

    print_str = '\n'
    result_tuple = validateInput(first_name, last_name, zip_code, employee_id)
    for result in result_tuple:
        print_str += result[1]

    if print_str == '\n':
        print_str += 'There were no errors found.'

    print (print_str)
