#! /usr/bin/python3

''' The function to search user name in the string.
'''

import re


def parsing_html():
    ''' Find the user name in the string.
    '''
    name = input("What is your name?: \n")
    # pattern = re.compile(r"\w+ (?=[is])")
    pattern = re.compile(r"([A-Za-z]+(?<=[is]))+?")
    result = pattern.findall(name)
    if result[0] == 'is':
        print("Hello {}".format(result[1]))
    else:
        print("Hello {}".format(result[0]))


parsing_html()
