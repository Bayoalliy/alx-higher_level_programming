#!/usr/bin/python3
"""
Write a Python script that fetches https://alx-intranet.hbtn.io/status

You must use the package urllib
You are not allowed to import any packages other than urllib
The body of the response must be displayed like the\
following example (tabulation before -)
You must use a with statement

guillaume@ubuntu:~/0x11$ ./0-hbtn_status.py | cat -e
Body response:$
    - type: <class 'bytes'>$
    - content: b'OK'$
    - utf8 content: OK$
guillaume@ubuntu:~/0x11$
"""

import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
    res = res.read()
    print("Body response:")
    print(f"\t- type: {type(res)}")
    print(f"\t- content: {res}")
    print(f"\t- utf8 content: {res.decode('utf-8')}")
