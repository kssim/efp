# Pratice 25. Password strength indicator
# Output:
#   The password '12345' is a very week password.
#   The password 'abcdef' is a week password.
#   The password 'abc123xyz' is a strong password.
#   The password '1337h@xor!' is a very strong password.
# Constraint:
#   - Create a 'passwordValidator' function that takes in the password
#     as its argument and returns a value you can evaluate to determine
#     the password strength.
#     Do not have the function return a string - you may need to support
#     multiple language in the future.
#   - Use a single output statement.

#!/usr/bin/env python

import sys
from re import search
from re import match

NORMAL_PWD      = 0
VERY_WEEK_PWD   = 1
WEEK_PWD        = 2
STRONG_PWD      = 3
VERY_STRONG_PWD = 4
STRONG_PWD_LENGTH_UNDER_LIMIT = 8

def input_process(in_question):
    return input(in_question) if sys.version_info >= (3,0) else raw_input(in_question)

def check_very_strong_pwd(in_str):
    return bool(search('[\d]+', in_str)) & bool(search('[\W]+', in_str)) & bool(search('[a-zA-Z]+', in_str)) & bool(len(in_str) >= STRONG_PWD_LENGTH_UNDER_LIMIT)

def check_strong_pwd(in_str):
    return bool(search('[\d]+', in_str)) & bool(search('[a-zA-Z]+', in_str)) & bool(len(in_str) >= STRONG_PWD_LENGTH_UNDER_LIMIT)

def check_weak_pwd(in_str):
    return bool(match('^[a-zA-Z]+$', in_str)) & bool(len(in_str) < STRONG_PWD_LENGTH_UNDER_LIMIT)

def check_very_weak_pwd(in_str):
    return bool(match('^[\d]+$', in_str)) & bool(len(in_str) < STRONG_PWD_LENGTH_UNDER_LIMIT)


def passwordValidator(in_pwd):
    if check_very_strong_pwd(in_pwd) == True:
        return VERY_STRONG_PWD
    elif check_strong_pwd(in_pwd) == True:
        return STRONG_PWD
    elif check_weak_pwd(in_pwd) == True:
        return WEEK_PWD
    elif check_very_weak_pwd(in_pwd) == True:
        return VERY_WEEK_PWD
    else:
        return NORMAL_PWD

if __name__ == '__main__':
    password = str(input_process('Input your password: '))

    result = passwordValidator(password)
    if result == VERY_WEEK_PWD:
        print ('The password \'%s\' is a very weak password.') % password
    elif result == WEEK_PWD:
        print ('The password \'%s\' is a weak password.') % password
    elif result == STRONG_PWD:
        print ('The password \'%s\' is a strong password.') % password
    elif result == VERY_STRONG_PWD:
        print ('The password \'%s\' is a very strong password.') % password
    elif result == NORMAL_PWD:
        print ('The password \'%s\' is a so so.') % password
