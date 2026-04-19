#!/usr/bin/python3

# Izračunati ukupan broj ECTS bodova

import subjects
import os, cgi
from http import cookies


params = cgi.FieldStorage()
cookie = cookies.SimpleCookie(os.environ.get('HTTP_COOKIE'))

def set_cookies(params, cookie):
    for key in subjects.subjects:
        if params.getvalue(key):
            cookie[key] = params.getvalue(key)

if os.environ['REQUEST_METHOD'].upper() == 'POST':
    set_cookies(params, cookie)
    print(cookie.output())
    print()

def create_checkboxes():
    for key, value in subjects.subjects.items():
        saved_value = cookie[key].value if key in cookie else "not"
        checked_enr = "checked" if saved_value == "Enrolled" and saved_value == params.getvalue(key) else "not"
        checked_not = "checked" if saved_value == "Not" and saved_value == params.getvalue(key) else "not"
        print(f'''
            <tr>
            <td><input type="checkbox" name="{key}" value={subjects.status_names.get("enr")} {checked_enr}>
            <input type="checkbox" name="{key}" value={subjects.status_names.get("not")} {checked_not}></td>
            <td>{value.get("name")}</td>
            <td>{value.get("ects")}</td>
    ''')
        
print(f'''
    <!DOCTYPE html>
      <html>
      <head><meta charset="UTF-8"></head>
      <body>
      <form action="test1.py" method="post" accept-charset="UTF-8">
      <table border=1>
''')

create_checkboxes()


def count_ects(ects):
    for key,value in subjects.subjects.items():
        if params.getvalue(key) == "Enrolled":
            ects += value.get("ects")
    return ects

ects = 0
ects = count_ects(ects)


print(f'''
      </table><br></br>
      <input type="submit" name="button" value="Spremi">
    </form>
      Upisao si {ects} bodova!
    </body>
    </html>
''')