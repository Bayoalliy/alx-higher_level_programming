#!/usr/bin/python3
"""
Write a Python script that fetches https://alx-intranet.hbtn.io/status

You must use the package requests
You are not allow to import packages other than requests
The body of the response must be display like
the following example (tabulation before -)


guillaume@ubuntu:~/0x11$ ./4-hbtn_status.py | cat -e
Body response:$
    - type: <class 'str'>$
    - content: OK$
guillaume@ubuntu:~/0x11$
"""

import requests

url = 'https://alx-intranet.hbtn.io/status'
res = requests.get(url)
print("Body response:")
print(f"\t- type: {type(res.text)}")
print(f"\t- content: {res.text}")
