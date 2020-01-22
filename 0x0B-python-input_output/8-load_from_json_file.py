#!/usr/bin/python3
"""
This is the "load_from_json_file" module.
This module contains function, load_from_json_file().
"""

from json import loads


def load_from_json_file(filename):
    """  Creates an Object from a “JSON file”."""

    with open(filename, 'r') as f:
        return loads(f.read())
        f.close()
