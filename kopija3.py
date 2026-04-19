#!/usr/bin/python3
import os, cgi, subjects
from http import cookies


params = cgi.FieldStorage()
cookie = cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))



def set_cookie(params, cookie):
    if params.getvalue("selectYear"):
        cookie["selectYear"] = params.getvalue("selectYear")


if os.environ['REQUEST_METHOD'].upper() == "POST":
    set_cookie(params, cookie)
    print(cookie.output())
    print()

def options():
    chosen = cookie["selectYear"].value if cookie["selectYear"] else ""
    
    for key, value in subjects.year_names.items():
        selected = "selected" if chosen == str(key) else ""
        print(f'''
            <option value="{key}" {selected}>{value}</option>
            ''')
    print('''</select>''')


def printSubjects(i):
    for value in subjects.subjects.values():
        if value.get("year") == i:
            print(f'''
                  <tr>
                  <td>{value.get("name")}<td>
                  </tr>
                  ''')

def checkYear():
    if params.getvalue("selectYear") == "1":
        printSubjects(1)
    elif params.getvalue("selectYear") == "2":
        printSubjects(2)
    elif params.getvalue("selectYear") == "3":
        printSubjects(3)

print(f'''
      <!DOCTYPE html>
        <html>
        <head></head>
        <body>
        <form action = "kopija3.py" method="post">
        <label for="selectYear">Choose a year:</label>
        <select name="selectYear" id="selectYear">
        ''')

options()

print('''
      <table border=1>
      ''')

checkYear()

print('''
      </table>
      <br>
      <input type="submit" name="button" value="spremi">
      </form>
      </body>
      </html>
      ''')
