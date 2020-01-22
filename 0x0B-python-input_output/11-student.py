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

    def to_json(self):
        """ Retrieves a dictionary representation of a Student instance."""
        return self.__dict__
