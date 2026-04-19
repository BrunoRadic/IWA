#!/usr/bin/python3
import cgi

params = cgi.FieldStorage()

name = params.getvalue("name")
pw1 = params.getvalue("pw1")
pw2 = params.getvalue("pw2")


print('''
    <!DOCTYPE html>
      <html>
      <head></head>
      <body>
      <form action = "lozinkica.py" method = "post">
''')

if not(name and pw1 and pw2) or pw1 != pw2:
    print('''
          <input type="text" name="name">
      <input type="password" name="pw1">
      <input type="password" name="pw2">
          <input type="submit" name="button" value="login">
          '''
          )
else:
    print("Hello WORLD!")



print('''
    
    </form>
    </body>
    </html>
      
''')    