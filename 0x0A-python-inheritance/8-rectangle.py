#!/usr/bin/python3
"""
This is the BaseGeometry module.
The BaseGeometry module contains functions, area(), integer_validator().
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


"""
This is the Rectangle module.
The Rectangle module defines the Rectangle class.
"""


class Rectangle(BaseGeometry):
    """ Rectangle class."""

    def __init__(self, width, height):
        """ Instatiation rectangle with width and height."""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
