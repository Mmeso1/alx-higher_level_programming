#!/usr/bin/python3
""" Rectangle Module """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ The class """

    def __init__(self, width, height):
        """ Intialization with validation """

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def ___ptr__(self):
        return (f"[Rectangle] {self.__width}/{self.__height}")

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
