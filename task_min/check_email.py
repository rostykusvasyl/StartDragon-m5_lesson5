#! /usr/bin/python3

''' Function for check email address'''

import re

def check_email():
    ''' check email address
    '''

    email_address = input("Input email address: \n")
    pattern = re.compile(r'[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-z]{2,}')
    result = pattern.search(email_address)

    if result is None:
        print('Bad Syntax !!!')
    else:
        print("This is a valid email address!")




check_email()
