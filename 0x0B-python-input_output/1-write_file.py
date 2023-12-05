#!/usr/bin/python3

""" Write to a file """


def write_file(filename="", text=""):
    """  writes a string to a text file (UTF8) and
    returns the number of characters written """
    with open(filename, 'w', encoding="utf-8") as f:
        num_of_chars = f.write(text)
        return num_of_chars
