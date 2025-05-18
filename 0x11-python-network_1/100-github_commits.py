#!/usr/bin/python3

"""
Write a Python script that takes 2 arguments in order to solve this challenge.

The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
"""
import requests
import sys

if __name__ == '__main__':
    repo = sys.argv[1]
    name = sys.argv[2]
    url = f"https://api.github.com/repos/{name}/{repo}/commits"
    data = {"owner": name, "repo": repo}
    res = requests.get(url, headers=data)
    res = res.json()
    for i in range(10):
        author_name = res[i].get('commit').get('author').get('name')
        print(res[i].get('sha'), end=": ")
        print(author_name)
