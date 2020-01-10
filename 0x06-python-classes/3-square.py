#!/usr/bin/python3


class Square:
    """class square
    Args:
        size (int): size of the square.
    Attributes:
        __size (int): size of square

    """

    def __init__(self, size=0):
        """class square
        Args:
            size (int): size of the square.
        Attributes:
            __size (int): size of square

        """

        if size < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            self.__size = size

    def area(self):
        """square the size
        Returns:
            Square of size.

        """

        return self.__size ** 2
