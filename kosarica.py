#!/usr/bin/python3
import os, cgi
from http import cookies
import articles

cookie = cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))

print()

print('''
<!DOCTYPE html>
<html>
<body>
<h2>Kosarica</h2>
''')

for k in articles.articles.values():
    if k.get("name") in cookie:
        print(f'''
        {cookie[k["name"]].key}<br>
        ''')

print('''
<br>
<a href="index.py">Back</a>
</body>
</html>
''')