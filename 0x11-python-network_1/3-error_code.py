#!/usr/bin/python3
"""  a Python script that fetches https://alx-intranet.hbtn.io/status """
from urllib import request, error
from sys import argv


if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as res:
            print(res.read().decode('utf-8'))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
