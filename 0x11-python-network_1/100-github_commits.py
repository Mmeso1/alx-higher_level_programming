#!/usr/bin/python3
"""
A Python script that list 10 commits (from the most recent to oldest)
"""
import requests
from sys import argv


if __name__ == "__main__":
    repo, owner = argv[1], argv[2]
    url = f"https://api.github.com/repos/{owner}/{argv[repo]}/commits"
    res = requests.get(url)
    data = res.json()
    for data in data[:10]:
        res = f"{data['sha']}: {data['commit']['author']['name']}"
        print(res)
