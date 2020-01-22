#!/usr/bin/python3
"""
This is the "read_file" module
This module contains function, read_file()
"""


def read_file(filename=""):
    """ Reads a text file (UTF8) and prints it to stdout."""

    with open(filename, 'r') as f:
        read_data = f.read()

    print('{:s}'.format(read_data), end='')

    f.closed
