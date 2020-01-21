#!/usr/bin/python3
"""
This is the MyInt module.
The MyInt module defines the MyInt class.
"""


class MyInt(int):
    """ Represent MyInt. class."""

    def __eq__(self, other):
        """ Returns if two MyInts are equal."""
        return int(self) != int(other)

    def __ne__(self, other):
        """ Returns two MyInts are not equal."""
        return int(self) == int(other)
