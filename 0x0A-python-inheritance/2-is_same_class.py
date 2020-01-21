#!/usr/bin/python3
"""
This is the "is same class" module.
The is same class module supplies one function, is_same_class().
"""


def is_same_class(obj, a_class):
    """ Returns True if the object is exactly an instance of the specified
        class, otherwise False.
    """
    return type(obj) is a_class
