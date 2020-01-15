#!/usr/bin/python3
"""
   This is the "Rectangle"  module
   This module provides a Rectangle class
"""


class Rectangle:
    """
    The Rectangle Class:
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Public instance method perimeter, returns perimeter of rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Public instance method perimeter, returns perimeter of rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * 2 + self.height * 2

    def __str__(self):
        """
           Public instance method str,
           print the rectangle with the character #:
        """
        if self.__width == 0 or self.__height == 0:
            return '{}'.format('')

        str_p = '#' * self.width
        return '\n'.join(list(str_p for i in range(self.height)))

    def __repr__(self):
        """
           Public instance method repr,
           return a string representation of the rectangle to be able to
           recreate a new instance
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """
            Prints after del instance
            using a print to method __del__,
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
