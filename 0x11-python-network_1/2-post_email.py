#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)

The email must be sent in the email variable
You must use the packages urllib and sys
You are not allowed to import packages other than urllib and sys
You don’t need to check arguments passed to the script (number or type)
You must use the with statement
"""
from urllib import request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = "email=" + sys.argv[2]
    email = email.encode('utf-8')
    Req = request.Request(url, email)
    with request.urlopen(Req) as res:
        res = res.read()
        print(res.decode('utf-8'))
