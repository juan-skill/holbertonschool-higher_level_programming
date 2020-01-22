#!/usr/bin/python3
"""
This is the Student module.
This module defines the Student class.
"""


class Student:
    """Represents a Student. Class."""

    def __init__(self, first_name, last_name, age):
        """ Initialize class."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student instance."""

        if attrs is None:
            return self.__dict__

        n_dictionary = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                n_dictionary[key] = value

        return n_dictionary
