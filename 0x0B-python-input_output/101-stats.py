#!/usr/bin/python3
""" Log parsing """


import sys

file_size = 0

status_code = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
        }


def print_metrics():
    print(f"File size: {file_size}")
    for scode, scode_count in sorted(status_code.items()):
        if scode_count > 0:
            print(f"{scode} : {scode_count}")


lc = 0

try:
    for line in sys.stdin:
        if lc != 0 and lc % 10 == 0:
            print_metrics()

        pieces = line.split()

        try:
            status = int(pieces[-2])

            if str(status) in status_code.keys():
                status_code[str(status)] += 1
        except Exception as e:
            pass

        try:
            file_size += int(pieces[-1])
        except Exception as e:
            pass

        lc += 1

    print_metrics()
except KeyboardInterrupt as e:
    print_metrics()
    raise e
