#!/usr/bin/python3

""" My List """


class MyList(list):
    """ Inherits from python list
    and printd the list in sorted order """

    def print_sorted(self):
        print(sorted(self))
