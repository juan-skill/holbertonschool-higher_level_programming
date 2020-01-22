#!/usr/bin/python3
"""
This is the "append_write" module
This module contains function, append_write
"""


def append_write(filename="", text=""):
    """ Appends a string at the end of a text file (UTF8) and returns the\
    number of characters added."""

    with open(filename, 'a', encoding='utf-8') as f:
        num = f.write(text)

    f.closed

    return num
