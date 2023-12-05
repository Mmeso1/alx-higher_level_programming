#!/usr/bin/python3
""" Square Module """


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """ The class """

    def __init__(self, size):
        """ Intialization with validation """

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
