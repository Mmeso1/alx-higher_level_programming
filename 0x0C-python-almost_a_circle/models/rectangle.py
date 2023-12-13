#!/usr/bin/python3

""" First Rectangle Module """

from models.base import Base


class Rectangle(Base):
    """ An inherited class from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        self.validate_arg("width", width)
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
        self.validate_arg("width", value)
        self.__width = value

    @property
    def height(self):
        """ getter for heigth """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height """
        self.validate_arg("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x."""
        self.validate_arg("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y."""
        self.validate_arg("y", value)
        self.__y = value

    def area(self):
        """
        ...
        """
        return self.__width * self.__height

    def validate_arg(self, attr_name, value):
        if type(value) is not int:
            raise TypeError(f"{attr_name} must be an integer")

        if attr_name == "height" or attr_name == "width":
            if value <= 0:
                raise ValueError(f"{attr_name} must be > 0")

        if attr_name == "x" or attr_name == "y":
            if value < 0:
                raise ValueError(f"{attr_name} must be >= 0")

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """
        attrs = ["id", "width", "height", "x", "y"]
        for i, arg in enumerate(args):
            if i < len(attrs):
                setattr(self, attrs[i], arg)

        for key, value in kwargs.items():
            if key in attrs:
                setattr(self, key, value)

    def display(self):
        for _ in range(self.__y):
            print()

        for _ in range(self.__height):
            print(" " * self.__x, end="")
            for _ in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height
                )

    def to_dictionary(self):
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
