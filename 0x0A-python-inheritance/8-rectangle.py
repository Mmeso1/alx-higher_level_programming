#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

""" Rectangle """


class Rectangle(BaseGeometry):
    """ The class """

    def __init__(self, width, height):
        """ Intialization with validation """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
