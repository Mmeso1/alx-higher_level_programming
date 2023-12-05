#!/usr/bin/python3

""" Load, add, save """
import sys
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item():
    filename = "add_item.json"

    if path.exists(filename):
        mylist = load_from_json_file(filename)
    else:
        mylist = []

    mylist.extend(sys.argv[1:])
    save_to_json_file(mylist, filename)

    if __name__ == "__main__":
        add_item()
