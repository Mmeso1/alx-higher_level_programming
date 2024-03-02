#!/usr/bin/python3
"""
A Python script that list 10 commits (from the most recent to oldest)
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    res = requests.get(url)
    data = res.json()
    for data in data[:10]:
        res = f"{data['sha']}: {data['commit']['author']['name']}"
        print(res)
