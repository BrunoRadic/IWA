#!/usr/bin/python3

# Dropdown za godinu

import os, cgi, subjects
from http import cookies


params = cgi.FieldStorage()
cookie = cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))

def set_cookie(params, cookie):
    if params.getvalue("selectedYear"):
        cookie["selectedYear"] = params.getvalue("selectedYear")


if os.environ['REQUEST_METHOD'].upper() == 'POST':
    set_cookie(params, cookie)
    print(cookie.output())
    print()



def selectPredmete():
    chosen = cookie.get("selectedYear")
    chosen = chosen.value if chosen else ""

    for key, value in subjects.year_names.items():
        selected = "selected" if str(key) == chosen else ""
        print(f'''
              <option value="{key}" {selected}>{value}</option>
              ''')
    print('''
          </select>
          <br>
          ''')
    
def printPredmete(k):
    for i in subjects.subjects.values():
            if i.get("year") == k:
                print(f'''
                    <tr>
                    <td>{i.get("name")}</td>
                    </tr>
                    ''')

def checkYear():
    if params.getvalue("selectedYear") == "1":
        printPredmete(1)
    elif params.getvalue("selectedYear") == "2":
        printPredmete(2)
    elif params.getvalue("selectedYear") == "3":
        printPredmete(3)
        
print('''
    <!DOCTYPE html>
      <html>
      <head></head>
      <body>
      <form action = "test3.py" method = "post">
      <label for="selectedYear">Choose a year:</label>
      <select name="selectedYear" id="selectedYear">
''')


selectPredmete()

print('''
    <table border=1>
''')

checkYear()

print('''
      </table>
      <br>
      <input type="submit" name="button" value="Submit">
    </form>
    </body>
    </html>
''')