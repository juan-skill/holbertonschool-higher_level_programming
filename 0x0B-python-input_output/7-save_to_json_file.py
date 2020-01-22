#!/usr/bin/python3
"""
This is the "save_to_json_file" module.
This module contains function, save_to_json_file().
"""

from json import dumps


def save_to_json_file(my_obj, filename):
    """  Writes an Object to a text file, using a JSON representation."""

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(dumps(my_obj))
        f.close()
