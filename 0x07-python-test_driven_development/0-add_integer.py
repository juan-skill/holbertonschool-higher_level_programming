#!/usr/bin/python3
"""
This is the "add integer" module.
The add integer module provide a function, add_integer()
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats as an Integer
    """

    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError('a must be an integer')
    if b is None or (type(b) is not int and type(b) is not float):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
