#!/usr/bin/python3
""" Takes my Github credentials (username and password)
and uses the Github API to display my Github id.
"""

import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://api.github.com/user'
    res = requests.post(url, auth=(argv[1], argv[2])).json()
    print(res.get('id'))
