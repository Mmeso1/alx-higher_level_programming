#!/usr/bin/python3

""" Geometry module """


class BaseGeometry:
    """  raises an Exception """
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ Validate the value """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
