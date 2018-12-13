#! /usr/bin/python3

''' Password Verification Program
'''

import re


def password_verification():
    ''' Check the password entered by the user.
    '''
    print('The password must contain at least one character from'
          'the following groups: (a-z), (A-Z), (0-9).')
    print("Must contain at least one character from the set: (* # @ +).")
    print("Length: 4 to 6 characters (no spaces).")
    while True:
        password = input('Input a strong password: \n')
        if re.match(r'^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)(?=.*[@*#+].*)'
                    r'[0-9a-zA-Z@*#+]{4,6}$', password):
            print('Very nice password.')
            break
        else:
            print('Not a valid password.')


password_verification()
