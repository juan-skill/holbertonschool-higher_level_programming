#!/usr/bin/python3
"""
This is the "inherits from" module.
The inherits from module contains, inherits_from().
"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that inherited
       the specified class ; otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
