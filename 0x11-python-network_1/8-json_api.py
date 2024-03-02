#!/usr/bin/python3
""" Search API """
import requests
from sys import argv

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    param = {'q': '' if len(argv) < 2 else argv[1]}
    res = requests.post(url, data=param)

    try:
        data = res.json()
        if (len(data) == 0):
            print("No result")
        else:
            print(f"{[data.get('id')]} {data.get('name')}")
    except ValueError:
        print("Not a valid JSON")
