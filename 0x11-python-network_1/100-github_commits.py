#!/usr/bin/python3
""" Please list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""

import requests
from sys import argv

if __name__ == '__main__':
    owner, repo = argv[1], argv[2]
    res = requests.get(f'https://api.github.com/repos/{owner}/{repo}/commits')
    data = res.json()

    for data in data[:10]:
        res = f"{data['sha']}: {data['commit']['author']['name']}"
        print(res)
