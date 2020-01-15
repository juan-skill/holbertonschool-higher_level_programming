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
    print_symbol = '#'

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

        str_p = str(self.print_symbol) * self.width
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
           Returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle) or \
           not isinstance(rect_2, Rectangle):

            wrong = "rect_1" if not isinstance(rect_1, Rectangle) else "rect_2"
            raise TypeError('{} must be an instance of Rectangle'
                            .format(wrong))

        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """
           Returns a new square instance
        """
        return Rectangle(size, size)
