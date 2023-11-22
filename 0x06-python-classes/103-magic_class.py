#!/usr/bin/python3
import math

class MagicClass:
    """A class representing a circle with magical properties.

    Attributes:
        __radius (int or float): The radius of the magical circle.

    Methods:
        __init__(self, radius): Initializes the MagicClass instance with a given radius.
        area(self): Calculates and returns the area of the magical circle.
        circumference(self): Calculates and returns the circumference of the magical circle.
    """
    def __init__(self, radius):
        """Initialize the MagicClass instance with a given radius.

        Args:
            radius (int or float): The radius of the magical circle.

        Raises:
            TypeError: If the provided radius is not an int or float.
        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """Calculate and return the area of the magical circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate and return the circumference of the magical circle."""
        return 2 * math.pi * self.__radius

