#!python.exe

import base, session, articles, os
from http import cookies


session_id, cookie = session.get_or_create_session_id()

session_data = session.get_session_data(session_id)

if cookie:
    print(cookie.output())
print()

def printBasket():

    if session_data.values() is not None:
        price = 0
        for key, value in articles.articles.items():

            if session_data.get(str(key)) == "yes":
                print(f'''
                      <p>{value["name"]}: {value["price"]}</p>
                      ''')
                price += value["price"]
            
        if price != 0:
         print(f"<p>Ukupna cijena: {price}</p>")
        else:
            print("Kosarica je prazna")

base.start_html()

printBasket()

base.finish_html()