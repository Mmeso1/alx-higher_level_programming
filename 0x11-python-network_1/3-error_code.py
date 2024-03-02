#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status """

from sys import argv
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError


if __name__ == "__main__":
    req = Request(argv[1])

    try:
        with urlopen(req) as res:
            print(res.read().decode('utf-8'))
        except HTTPError as err:
            print('Error code:', err.code)
