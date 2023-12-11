#!/usr/bin/python3

""" Base Class Module """

import json
import csv
import turtle


class Base:
    """ The base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int): The identity of the instance.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """Converts a list of objects to a JSON string"""
        if not list_dictionaries:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        class_name = cls.__name__

        if list_objs is None:
            list_objs = []

        list_dictionaries = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dictionaries)

        with open(f"{class_name}.json", 'w', encoding="utf-8") as f:
            f.write(json_string)

    def from_json_string(json_string):
        """ returns the list of the JSON string
        representation json_string """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        dummy_instance = cls(2, 3)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        filename = f"{cls.__name__}.json"

        try:
            with open(filename, 'r', encoding="utf-8") as f:
                json_data = f.read()
                if json_data:
                    json_dicts = cls.from_json_string(json_data)
                    instances = [cls.create(**dic) for dic in json_dicts]
                    return instances
                else:
                    return []
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Basically, an object is given, convert it to a dictionary
        then using the csv module, write the data in the dictionary to a file
        """

        filename = f"{cls.__name__}.csv"

        if list_objs is None or len(list_objs) == 0:
            list_objs = []

        list_dictionaries = [obj.to_dictionary() for obj in list_objs]

        with open(filename, 'w', encoding="utf-8") as f:
            csv_writer = csv.writer(f)

            if cls.__name__ == "Rectangle":
                csv_writer.writerow(["id", "width", "height", "x", "y"])
            elif cls.__name__ == "Square":
                csv_writer.writerow(["id", "size", "x", "y"])

            for obj in list_objs:
                csv_writer.writerow([
                    getattr(obj, key) for key in obj.to_dictionary().keys()
                    ])

    @classmethod
    def load_from_file_csv(cls):
        filename = f"{cls.__name__}.csv"
        instances = []

        try:
            with open(filename, 'r', encoding="utf-8") as f:
                csv_reader = csv.reader(f)
                header = next(csv_reader)

                for row in csv_reader:
                    data = {header[i]: int(row[i]) for i in range(len(header))}
                    instance = cls.create(**data)
                    instances.append(instance)
        except FileNotFoundError:
            return []
        return instances

    def draw(list_rectangles, list_squares):
        """ Turtle game functions, yayyy!!! """
        """ Thought I was going to see an actual turtle,
        turns out it is just an arrow drawing the squares.
        Not so satisfying and saddening """
        screen = turtle.Screen()
        screen.bgcolor("white")

        """ Draw Rectangles """
        for rectangle in list_rectangles:
            Base.draw_rectangle(rectangle)

        for square in list_squares:
            Base.draw_square(square)

        turtle.done()

    def draw_rectangle(rectangle):
        t = turtle.Turtle()
        t.penup()
        t.goto(rectangle.x, rectangle.y)
        t.pendown()

        for _ in range(2):
            t.forward(rectangle.width)
            t.left(90)
            t.forward(rectangle.height)
            t.left(90)
        t.hideturtle()

    def draw_square(square):
        t = turtle.Turtle()
        t.penup()
        t.goto(square.x, square.y)
        t.pendown()

        for _ in range(4):
            t.forward(square.size)
            t.left(90)
        t.hideturtle()
