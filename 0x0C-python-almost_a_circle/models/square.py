#!/usr/bin/python3

""" The Square module """

from models.rectangle import Rectangle, validate_arg


class Square(Rectangle):
    """ The Square Class """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ to get size """
        return self.width

    @size.setter
    def size(self, size):
        """ to set size """
        validate_arg("width", size)
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ To update the attrs of this class """
        attrs = ["id", "size", "x", "y"]
        for i, arg in enumerate(args):
            if i < len(attrs):
                setattr(self, attrs[i], arg)

        for key, value in kwargs.items():
            if key in attrs:
                setattr(self, key, value)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
