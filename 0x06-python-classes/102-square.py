#!/usr/bin/python3


class Square:
    """class square
    Args:
        size (int): size of the square.
    Attributes:
        __size (int): size of square
    """

    def __init__(self, size=0):
        """"Initialize class
        Args:
            size (int): size of the square.
        Attributes:
            __size (int): size of square
        """
        self.__size = size

    @property
    def size(self):
        """size properties
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size setter
        Args:
            value (int): size of the square.
        Attributes:
            __size (int): size of square
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """square the size
        Returns:
            Square of size.
        """

        return self.__size ** 2

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __gt__(self, other):
        return self.area() > other.area()
