#!/usr/bin/python3
import subjects, cgi, os
from http import cookies

params = cgi.FieldStorage()
cookie = cookies.SimpleCookie(os.environ.get('HTTP_COOKIE'))


def set_cookie(params, cookie):
    
    for key in subjects.subjects:
        value = params.getvalue(key)

        if value:
            cookie[key] = value
        else:
            cookie[key] = ""
            cookie[key]["Max-Age"] = 0



if os.environ['REQUEST_METHOD'].upper() == "POST":
    set_cookie(params,cookie)
    print(cookie.output())
    print()


def create_checkboxes():
    for key, value in subjects.subjects.items():
        saved_value = cookie[key].value if key in cookie else ""
        checked = "checked" if saved_value else ""
        print(f'''
              {value.get("name")}
              <input type="checkbox" name={key} value="True" {checked}>
              <br>
              ''')

print(f'''
    <!DOCTYPE html>
      <html>
      <head><meta charset="UTF-8"></head>
      <body>
      <form method="post" action="subjekti.py" accept-charset="UTF-8">
      ''')


create_checkboxes()



print('''
    <input type="submit" name="button" value="Spremi">
      <br>
      <br>
    <a href="oznaceni.py">Oznaceni</a> 
    </form>
      </body>
      </html>
      ''')


