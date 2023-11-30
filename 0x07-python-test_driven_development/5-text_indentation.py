#!/usr/bin/python3

""" Text Indentation """


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters:
    ., ? and :
    """

    if type(text) is not str:
        raise TypeError('text must be a string')

    flag = 0
    for char in text:
        if flag == 0:
            if char == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if char in ['.', '?', ':']:
                print(char)
                print()
                flag = 0
            else:
                print(char, end="")
