#!/usr/bin/python3

import base, articles, session


session_id, cookie = session.get_or_create_session_id()

data = session.get_session_data(session_id)


if cookie:
    print(cookie.output())
print()


def printArticles():

    if data:
        for key, value in articles.articles.items():
            if data.get(key) == "Yes":
                print(f'''
                    {value["name"]}<br>
    
''')
    else:
        print("Kosarica je prazna.")

base.start_html()


printArticles()

base.end_html()

