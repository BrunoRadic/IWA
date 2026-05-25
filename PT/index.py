#!/usr/bin/python3


import base, os, db, session, articles, cgi
from http import cookies

params = cgi.FieldStorage()

session_id, cookie = session.get_or_create_session_id()

if os.environ.get("REQUEST_METHOD").upper() == "POST":
    session.save_articles(session_id, params)
    print("Location: kosarica.py")
    print()
    exit()

session_data = session.get_session_data(session_id)

print("Content-Type: text/html")
if cookie:
    print(cookie.output())
print()

def printCheckbox():

    for key, value in articles.articles.items():
        saved_value = session_data.get(key)
        checked = "checked" if saved_value == "Yes" else ""
        print(f'''
        {value["name"]}<input type="checkbox" name={key} value="Yes" {checked}><br>

''')

base.start_html()


printCheckbox()

print('''
            <input type="submit" name="button" value="Spremi"> 
      ''')

base.end_html()