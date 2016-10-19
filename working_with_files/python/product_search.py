# Pratice 44. Product Search
# Output:
#   What is the product name? iPad
#   Sorry, that product was not found in our inventory.
#   What is the product name? Widget
#   Name : Widget
#   Price : $25.00
#   Quantity on hand : 5
# Constraint:
#   - The file is in the JSON format.
#     Use a JSON parser to pull the values out of the file.
#   - If no record is found, prompt again.

#!/usr/bin/env python

import sys
from json import loads

FILE_NAME = 'product_search.json'

def input_process(in_question):
    return input(in_question) if sys.version_info >= (3,0) else raw_input(in_question)

def get_json_data():
    try:
        with open(FILE_NAME, 'r') as f:
            return loads(f.read())
    except:
        print ('File does not created.')
        exit()

    return {}

def print_data(data):
    print ('Name: %s' % data['name'])
    print ('Price: %s' % data['price'])
    print ('Quantity on hand: %s' % data['quantity'])

if __name__ == '__main__':
    data_list = get_json_data()
    if len(data_list) == 0:
        print ('Data is empty.')
        exit()

    while True:
        product_name = str(input_process('What is the product name? '))
        for data in data_list['products']:
            if data['name'] == product_name:
                print_data(data)
                exit()

        print ('Sorry that product was not found in our inventory.')
