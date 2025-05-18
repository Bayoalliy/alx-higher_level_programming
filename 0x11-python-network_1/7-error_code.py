#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request
to the URL and displays the body of the response.

If the HTTP status code is greater than or equal to 400,
print: Error code: followed by the value of the HTTP status code
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    res = requests.get(url)
    if int(res.status_code) >= 400:
        print(f"Error code: {res.status_code}")
    else:
        print(res.text)
