#!/usr/bin/python3

# Dodijeliti status svakom predmetu.

import os, cgi, subjects
from http import cookies

params = cgi.FieldStorage()
cookie = cookies.SimpleCookie(os.environ.get('HTTP_COOKIE'))

def set_cookie(params, cookie):
    for key in subjects.subjects:
        if params.getvalue(key):
            cookie[key] = params.getvalue(key)

if os.environ['REQUEST_METHOD'].upper() == 'POST':
    set_cookie(params, cookie)
    print(cookie.output())
    print()


def printRadio():
    for key, value in subjects.subjects.items():
        saved_value = cookie[key].value if key in cookie else "null"
        checked_enr = "checked" if saved_value == "enr" else "null"
        checked_pass = "checked" if saved_value == "pass" else "null"
        checked_not = "checked" if saved_value == "not" else "null"
        print(f'''
              <tr>
              <td>
              {value.get("name")}
              </td>
              <td>
            <input type="radio" name={key} value="enr" {checked_enr} >{subjects.status_names.get("enr")}
            <input type="radio" name={key} value="pass" {checked_pass} >{subjects.status_names.get("pass")}
            <input type="radio" name={key} value="not" {checked_not} >{subjects.status_names.get("not")}
            </td>
        '''
        )
        


print(f'<td>Ovajjjjj je los nacin lowkey</td>')
print(f'<td>Sine...</td>')
#zamini s
print(f'''
      <td>Ovajjjjj je los nacin lowkey</td>
      <td>Sine...</td>
      ''')


print('''
    <!DOCTYPE html>
      <html>
      <head></head>
      <body>
      <form action="test2.py" method="post">
      <table border=1>
      
''')

printRadio()

print('''
      </table>
      <input type="submit" name="button" value="Submit">
    </form>
    </body>
    </html>
''')