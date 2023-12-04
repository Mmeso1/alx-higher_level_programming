#!/usr/bin/python3

""" Only sub class of """


def inherits_from(obj, a_class):
    """
    returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class;
    otherwise False.
    """

    def inherits_from(obj, a_class):
        return issubclass(obj, a_class)
