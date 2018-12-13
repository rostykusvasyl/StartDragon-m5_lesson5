#! /usr/bin/python3

''' Function for check phone number'''

import re

def check_phone_number():
    ''' check the phone number
    '''
    phone_number = input("Enter the phone number in the"
                         "format:(xxx)xxx-xxxx \n")
    pattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})$')
    result = pattern.search(phone_number)

    if result is None:
        print('Bad Syntax !!!')
    else:
        print("This is a valid phone number!")


check_phone_number()
