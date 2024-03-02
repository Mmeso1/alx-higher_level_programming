#!/usr/bin/python3
"""  POST an email """

from urllib.request import Request, urlopen
import urllib.parse as parse
from sys import argv

if __name__ == "__main__":
    data = parse.urlencode({'email': argv[2]}).encode()
    req = Request(argv[1], data=data)

    with urlopen(req) as res:
        print(res.read().decode('utf-8'))
