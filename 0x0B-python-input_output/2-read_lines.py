#!/usr/bin/python3
"""
This is the "read_lines" module
This module contains function, read_lines()
"""


def read_lines(filename="", nb_lines=0):
    """ Reads n lines of a text file (UTF8) and prints it to stdout."""

    with open(filename, 'r') as f:

        if nb_lines == 0:
            print('{:s}'.format(f.read()), end='')
            return

        for count, line in enumerate(f, 1):
            if count < nb_lines:
                print(line, end='')
