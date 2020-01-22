#!/usr/bin/python3
"""
This is the "read_lines" module
This module contains function, read_lines()
"""


def write_file(filename="", text=""):
    """ Writes a string to a text file (UTF8) \
    and returns the number of characters written
    """

    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
