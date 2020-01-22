#!/usr/bin/python3
"""
This is the "6-from_json" module.
This module contains function, from_json_string().
"""

from json import loads


def from_json_string(my_obj):
    """ Returns an object (P. data structure) represented by a JSON string:"""

    return loads(my_obj)
