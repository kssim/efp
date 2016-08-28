# Pratice 3. Printing Quotes
# Output:
#   What is the quote? Books are a uniquely portable magic.
#   Who said it? Stephen King
#   Stephen King says, "Books are a uniquely portable magic."
# Constraint:
#   - Use a single output statement to produce this output,
#     using appropriate string-escaping techniques for quotes.
#   - If your language supports string interpolation or string
#     substitution, don't use it for this exercise. Use string
#     concatenation instead.

#!/usr/bin/env python

import sys

def input_process(in_question):
    return input(in_question) if sys.version_info >= (3,0) else raw_input(in_question)


if __name__ == '__main__':
    quotation = input_process('What is the quote? ')
    author = input_process('Who said it? ')

    print_str = author
    print_str += ' says, \"'
    print_str += quotation
    print_str += '\"'

    print (print_str)
