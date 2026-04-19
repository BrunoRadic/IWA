#!/usr/bin/python3
import subjects, os
from http import cookies

cookie = cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))

print(f'''
    <!DOCTYPE html>
      <html>
      <head><meta charset="UTF-8"></head>
      <body>
      ''')

for key, value in subjects.subjects.items():
    if key in cookie:
        print(f'''
              {value.get("name")}
            <br>
              ''')

print('''
    <a href="subjekti.py">Back</a> 
    </form>
    </body>
    </html>
      ''')


