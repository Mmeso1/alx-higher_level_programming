#!/usr/bin/python3
import sys

file_size = 0

status_code = {
        "200" : 0,
        "301" : 0,
        "400" : 0,
        "401" : 0,
        "403" : 0,
        "404" : 0,
        "405" : 0,
        "500" : 0
        }

def print_metrics():
    print(f"File size: {file_size}")
    for scode, scode_count in sorted(status_code.items()):
        if scode_count > 0:
            print(f"{scode} : {scode_count}")

line_count = 0

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            file_size = int(parts[-1])
            code = parts[-2]

            if code in status_code.keys():
                status_code[code] += 1

            line_count += 1

            if line_count > 10:
                line_count = 0
                print_metrics()

        except KeyboardInterrupt:
            print_metrics()
            raise
except:
    pass
