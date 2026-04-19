#!/usr/bin/python3


import os, cgi, subjects
from http import cookies

params = cgi.FieldStorage()
cookie = cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))


def set_cookie(params, cookie):
    for key in subjects.subjects:
        if params.getvalue(key):
            cookie[key] = params.getvalue(key)

if os.environ['REQUEST_METHOD'].upper() == "POST":
    set_cookie(params,cookie)
    print(cookie.output())
    print()



def create_checkbox():
    for key, value in subjects.subjects.items():
        saved_value = cookie[key].value if key in cookie else ""
        checked = "checked" if saved_value == params.getvalue(key) else ""
        print(f'''
              <tr>
            <td><input type="checkbox" name="{key}" value={subjects.status_names.get("enr")} {checked}></td>
            <td>{value.get("name")}</td>
            <td>{value.get("ects")}</td>
            </tr>
              ''')


print('''
      <!DOCTYPE html>
      <html>
      <head></head>
      <body>
      <form action="kopiaj1.py" method="post">
      <table border=1>
      ''')


create_checkbox()

def count_ects(ects):
    for key, value in subjects.subjects.items():
        if params.getvalue(key):
            ects+= value.get("ects")
    return ects

ects=0
ects = count_ects(ects)

print(f'''
      </table>
      <input type="submit" name="button" value="Send">
    </form>
      {ects}
      </body>
      </html>
''')
