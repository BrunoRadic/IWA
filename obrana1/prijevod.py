#!python.exe

import base, translations, cgi, os
from http import cookies

params = cgi.FieldStorage()
cookie = cookies.SimpleCookie(os.environ.get('HTTP_COOKIE'))

def set_cookie(params, cookie):

    cookie['radio'] = 'eng'
    if params.getvalue('radio'):
        cookie['radio'] = params.getvalue('radio')


if os.environ['REQUEST_METHOD'].upper() == 'POST':
    set_cookie(params, cookie)
    print(cookie.output())
    print()

print("Content-Type: text/html")
base.start_html()

def printTable():
    selected = cookie["radio"].value if "radio" in cookie else "eng"
    for key, value in translations.translations.items():
        if key == selected:
            print(f'''
                  <a href="index.py"> {value["index"]}</a>
                  <a href="articles.py"> {value["articles"]}</a>
                  <a href="contact.py"> {value["contact"]}</a>
                  <a href="basket.py"> {value["basket"]}</a>
                  ''')

print('<div>')
printTable()
print('</div>')

base.end_html()