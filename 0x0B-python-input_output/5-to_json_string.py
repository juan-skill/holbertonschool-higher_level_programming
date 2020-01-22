#!/usr/bin/python3
"""
This is the "to_json_string" module.
This module contains function, to_json_string().
"""

from json import dumps


def to_json_string(my_obj):
    """  Returns the JSON representation of an object (string)."""

    return dumps(my_obj)
