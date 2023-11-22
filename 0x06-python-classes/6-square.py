#!/usr/bin/python3

"""This is the square class"""


class Square:
    """Square class that defines a square by: (based on 1-square.py)"""
    def __init__(self, size=0, position=(0, 0)):
        """__init__
        The init method is like a constructor, it initializes the class
        with the size value of the square

        Attributes:
            size(int): the size of the square

        Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
        """

        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
        self.__position = position

    def area(self):
        """area
        The method returns the area of the square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """size
        a getter function to retrieve the value of the private attribute `size`
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size
        this one is to set the value of the private attribute `size`
        """

        if type(value) is not int:
            raise TypeError('size must be an integer')

        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    @property
    def position(self):
        """Returns the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square

        Args:
        value (tuple): The position of the square.

        Raises:
            TypeError: If value is not a tuple.
            ValueError: If value is not a tuple of 2 positive integers.

        Returns:
            None
        """
        if (
                not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                value[0] < 0 or
                value[1] < 0
                ):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def my_print(self):
        """my_print
        Public instance method to print the square.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
