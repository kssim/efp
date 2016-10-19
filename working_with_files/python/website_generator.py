# Pratice 42. Website Generator
# Output:
#   Site name: awesomeco
#   Author: Max Power
#   Do you want a folder for JavaScript? y
#   Do you want a folder for CSS? y
#   Created ./awesomeco
#   Created ./awesomeco/index.html
#   Created ./awesomeco/js/
#   Created ./awesomeco/css/
# Constraint:
#   - Generate an index.html file that contains the name of the site inside the <title> tag and the author in a <meta> tag.

#!/usr/bin/env python

import sys
from os import makedirs

def input_process(in_question):
    return input(in_question) if sys.version_info >= (3,0) else raw_input(in_question)

def create_index_file(site_name, author):
    file_name = '%s/index.html' % site_name

    try:
        with open(file_name, 'w') as f:
            f.write('<title>%s</title>\n' % site_name)
            f.write('<meta>author:%s</meta>' % author)
    except:
        print ('File does not created.')
        exit()


if __name__ == '__main__':
    site_name = str(input_process('Site name: '))
    author = str(input_process('Author: '))
    create_js_dir = str(input_process('Do you want a folder for JavaScript?(y) '))
    create_css_dir = str(input_process('Do you want a folder for CSS?(y) '))

    makedirs(site_name)
    create_index_file(site_name, author)

    if create_js_dir.upper() == 'Y':
        makedirs('%s/js' % site_name)

    if create_css_dir.upper() == 'Y':
        makedirs('%s/css' % site_name)

    print ('Website skeleton was created.')
