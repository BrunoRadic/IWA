#!python.exe

import base, cgi, session, articles, os
from http import cookies

params = cgi.FieldStorage()

session_id, cookie = session.get_or_create_session_id()

if os.environ.get("REQUEST_METHOD").upper() == "POST":
    session.saveArticles(session_id, params)
    print("Location: kosarica.py")
    print()
    exit()

session_data = session.get_session_data(session_id)

print("Content-Type: text/html")
if cookie:
    print(cookie.output())
print()

def printArticles():

    for key, value in articles.articles.items():
        name = value["name"]
        checked = "checked" if session_data.get(str(key)) == "yes" else ""
        print(f'''
        {name}<input type="checkbox" name={key} value="yes" {checked}><br>

''')

base.start_html()
print('''<form method="post" action="">''')
printArticles()


print('''
        <input type="submit" name="button" value="Spremi">
      ''')
print("</form>")
base.finish_html()