#!/usr/bin/python3

def uppercase(str):
    for i in str:
        if 97 <= ord(i) <= 122:
            return chr(ord(i - 32))
