#!python.exe

import base, translations, cgi, os
from http import cookies

params = cgi.FieldStorage()
cookie = cookies.SimpleCookie(os.environ.get('HTTP_COOKIE'))


print("Content-Type: text/html")
base.start_html()
print('''<form action="prijevod.py" method="post">''')



def printRadios():

    saved_value = cookie['radio'].value if "radio" in cookie else ""
    for i in translations.translations:
            print(f'''
                <input type="radio" name="radio" value="{i}" {"checked" if saved_value == i else ""}>{i}<br>
                ''')

print('''
    <div>
      <a href="index.py"> index </a>
      <a href="articles.py"> articles </a>
      <a href="basket.py"> basket </a>
      <a href="contact.py"> contact </a>
    </div>
''')

printRadios()

print('''
    <input type="submit" name="button" value="Next">
      </form>
    <a href="prijevod.py">Prijevod</a>
''')




base.end_html()