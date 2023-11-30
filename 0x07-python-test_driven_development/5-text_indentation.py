#!/usr/bin/python3

""" Text Indentation """


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: 
    ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    txt = ""
    for char in text:
        if char in ['.', '?', ':']:
            txt += char + '$' + '\n' + '$' + '\n'
        else:
            if char == ' ':
                continue
            txt += char
    print(txt)
