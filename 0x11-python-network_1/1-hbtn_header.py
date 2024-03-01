#!/usr/bin/python3
"""Response header value """

from sys import argv
from urllib.request import Request, urlopen

if __name__ == "__main__":
    url = argv[1]
    req = Request(url)

    with urlopen(req) as response:
        print(response.headers.get('X-Request-Id'))
