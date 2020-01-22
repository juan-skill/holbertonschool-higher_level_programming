#!/usr/bin/python3
"""
This is the "number_of_lines" module
This module contains function, number_of_lines()
"""


def number_of_lines(filename=""):
    """ Returns the number of lines of a text file."""

    with open(filename, 'r') as f:
        for count, line in enumerate(f, 1):
            pass

    f.closed

    return count
