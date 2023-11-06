#!/usr/bin/python3

def no_c(my_string):
    str = ""

    for char in my_string:
        if char in 'cC':
            continue
        str += char
    return (str)
