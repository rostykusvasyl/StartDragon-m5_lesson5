#! /usr/bin/python3

''' The function to search the text in this tag on the html page.
'''

import re

HTML_PAGE = ('<html lang="en-US" xmlns="http://www.w3.org/1999/xhtml" '
             'xml:lang="en-US">'
             '<head>'
             '<meta http-equiv="content-type" content="text/html;'
             'charset=us-ascii" /> <title>Turtle Soup</title> </head> '
             '<body> <h1>Adjust the Project Settings</h1> </body> </html>')

def parsing_html():
    ''' Find text between tags.
    '''
    pattern = re.compile(r"(?is)<title[^>]*>(.+?)</title>")
    result = pattern.findall(HTML_PAGE)
    print(result[0])

parsing_html()
