#!/usr/bin/python3
"""
Write a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id

You must use Basic Authentication with a personal access token as
password to access to your information (only read:user permission is needed)
The first argument will be your username
The second argument will be your password (in your case,
a personal access token as password)
You must use the package requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
"""
import requests
import sys

if __name__ == '__main__':
    url = "https://api.github.com/user"
    token = "token " + sys.argv[2]
    data = {"Authorization": token, "name": sys.argv[1]}
    res = requests.get(url, headers=data)
    res = res.json()
    print(res.get('id'))
