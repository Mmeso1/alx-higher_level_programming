#!/usr/bin/python3

""" Class to JSON """


def class_to_json(obj):
    """ returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON
    serialization of an object """

    serializable_dict = {}

    for attribute_name, attribute_value in obj.__dict__.items():
        if isinstance(attribute_value, (list, dict, str, int, bool)):
            serializable_dict[attribute_name] = attribute_value
    return serializable_dict
