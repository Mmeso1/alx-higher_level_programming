#!/usr/bin/python3

""" Append to a file """


def append_write(filename="", text=""):
    """  appends a string at the end of a text file (UTF8)
    and returns the number of characters added """

    with open(filename, 'a', encoding="utf-8") as f:
        added_chars_num = f.append(text)
        return added_chars_num
