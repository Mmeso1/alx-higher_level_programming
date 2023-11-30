#!/usr/bin/python3

""" Text Indentation """


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters:
    ., ? and :
    """

    if type(text) is not str:
        raise TypeError('text must be a string')

    for i, char in enumerate(text):
        if char in ['.', '?', ':']:
            print(char)
            print()
        elif char != ' ':
            print(char, end='')
