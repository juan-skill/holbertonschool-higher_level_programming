#!/usr/bin/python3
"""
This is the BaseGeometry module.
The BaseGeometry module contains two functions, area() and integer_validator().
"""
Rectangle = __import__('9-rectangle').Rectangle


"""
This is the Square module.
The Square module defines the Square class.
"""


class Square(Rectangle):
    """ Square class."""

    def __init__(self, size):
        """ Instatiation square with size."""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """ Return the width and height of the square."""
        return ('[Rectangle] {:d}/{:d}'.format(self.__size, self.__size))
