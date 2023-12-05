#!/usr/bin/python3

""" Can I? (Be a new attribute """


def add_attribute(obj, name, value):
    """ Add new attribute to object """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
