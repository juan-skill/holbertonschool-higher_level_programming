#!/usr/bin/python3
"""This class is the base class"""


import json


class Base:
    """Base class for all other modules
    Attributes:
        __nb_objects: private attribute to count objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation of base class
        Args:
            id: input id
        Attributes:
            id: public instance id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Return the JSON string representation of list_dictionaries."""
        if not list_dictionaries or list_dictionaries is None:
            return '[]'

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file."""

        if list_objs is None:
            my_list = []
        else:
            my_list = [objs.to_dictionary() for objs in list_objs]

        filename = '{}.json'.format(cls.__name__)
        with open(filename, mode='w', encoding='UTF-8') as f:
            f.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """ Represent the list of the JSON string representation
        json_string."""

        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """  Return an instance with all attributes already set."""

        dummy = cls(1, 1) if cls.__name__ == 'Rectangle' else cls(1)
        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances."""

        try:
            filename = '{}.json'.format(cls.__name__)
            with open(filename, mode='r', encoding='UTF-8') as f:
                return [cls.create(**objs)
                        for objs in cls.from_json_string(f.read())]
        except Exception:
            return []
