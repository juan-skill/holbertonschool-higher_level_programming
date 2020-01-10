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

    def my_print(self):
        """print the square
        Returns:
           void
       """
        if self.__size is 0:
            print("")
        for i in range(self.__size):
            print("#" * self.__size)
