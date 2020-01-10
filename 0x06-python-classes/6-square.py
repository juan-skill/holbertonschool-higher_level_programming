#!/usr/bin/python3


class Square:
    """class square
    Args:
        size (int): size of the square.
    Attributes:
        __size (int): size of square
    """

    def __init__(self, size=0, position=(0, 0)):
        """"Initialize class
        Args:
            size (int): size of the square.
            position (set): coordinates
        Attributes:
            __size (int): size of square
            position (set): coodinates
        """
        self.__size = size
        self.position = position

    @property
    def size(self):
        """size properties
        """
        return self.__size

    @property
    def position(self):
        """position properties
        """
        return self.__position

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

    @position.setter
    def position(self, value):
        """position setter
        Args:
           value (tuple): position
        Attributes:
           __position (tuple): position

        """
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not(type(value[0]) is int and type(value[1]) is int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
