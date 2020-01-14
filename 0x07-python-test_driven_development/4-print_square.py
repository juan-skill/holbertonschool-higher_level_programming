#!/usr/bin/python3

"""
Print Square module, for printing squares.
This module contains the following functions: print_square
"""


def print_square(size):
    """
        Print a square with the character #
    """

    if not isinstance(size, (int)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return

    for i in range(int(size)):
        print("#" * int(size))
