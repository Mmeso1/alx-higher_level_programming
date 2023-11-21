#!/usr/bin/python3

"""This is the square class"""


class Square:
    """Square class that defines a square by: (based on 0-square.py)"""
    def __init__(self, size):
        """__init__
        The init method is like a constructor, it initializes the class
        with the size value of the square

        Attributes:
            size: the size of the square
        """

        self.__size = size
