#!/usr/bin/python3

""" First Rectangle Module """
from models.base import Base


def validate_arg(attr_name, value):
    if not isinstance(value, int):
        raise TypeError(f"{attr_name} must be an integer")

    if attr_name == "height" or attr_name == "width":
        if value <= 0:
            raise TypeError(f"{attr_name} must be > 0")

    if attr_name == "x" or attr_name == "y":
        if value < 0:
            raise ValueError(f"{attr_name} must be >= 0")


class Rectangle(Base):
    """ An inherited class from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ getter func for width """
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width """
        if validate_arg("width", value):
            self.__width = value

    @property
    def height(self):
        """ getter for heigth """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height """
        if validate_arg("height", value):
            self.__height = value

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x."""
        if validate_arg("x", value):
            self.__x = value

    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y."""
        if validate_arg("y", value):
            self.__y = value

    def area(self):
        """
        ...
        """
        return self.__width * self.__height

    def display(self):
        for _ in range(self.__height):
            for _ in range(self.__width):
                print("#", end="") 
            print()
