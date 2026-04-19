#!/usr/bin/python3
import articles, cgi, os
from http import cookies

params = cgi.FieldStorage()
cookie = cookies.SimpleCookie(os.environ.get('HTTP_COOKIE'))


def set_cookies(params, cookie):
    for item in articles.articles.values():
        name = item.get("name")
        if params.getvalue(name):
            cookie[name] = params.getvalue(name)
        else:
            if name in cookie:
                cookie[name] = ""
                cookie[name]["Max-Age"] = 0 

if os.environ['REQUEST_METHOD'].upper() == 'POST':
    set_cookies(params, cookie)
    print(cookie.output())
    print()


def create_checkbox():
    for i in articles.articles.values():
        saved_value = cookie[i.get("name")].value if i.get("name") in cookie else ""
        checked = "checked" if saved_value else "" 
        print(f'''
              {i.get("name")}
              <input type="checkbox" name="{i.get("name")}" value="true" {checked}>
              <br>
              ''')


print(f'''
    <!DOCTYPE html>
      <html>
      <head><meta charset="UTF-8"></head>
      <body>
      <form method="post" action="index.py" accept-charset="UTF-8">
      ''')




create_checkbox()


print('''
    <input type="submit" name="button" value="Spremi">
      <br>
      <br>
    <a href="kosarica.py">Kosarica</a> 
    </form>
      </body>
      </html>
      ''')


