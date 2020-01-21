#!/usr/bin/python3
"""
This is the BaseGeometry module.
The BaseGeometry module contains, area(), integer_validator().
"""


class BaseGeometry:
    """Represents a BaseGeometry. Class."""

    def area(self):
        """Raise an exception."""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validate integers."""
        if type(value) is not int:
            raise TypeError('{:s} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
