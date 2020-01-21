#!/usr/bin/python3
"""
This is the BaseGeometry module.
The BaseGeometry module contains functions, area(), integer_validator().
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


"""
This is the Rectangle module.
The Rectangle module contains functions, area(), __repr__.
"""


class Rectangle(BaseGeometry):
    """ Rectangle class."""

    def __init__(self, width, height):
        """ Instatiation rectangle with width and height."""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Return the area of the rectangle."""
        return self.__width * self.__height

    def __repr__(self):
        """ Print the width and height of the rectangle."""
        return ('[Rectangle] {:d}/{:d}'.format(self.__width, self.__height))
