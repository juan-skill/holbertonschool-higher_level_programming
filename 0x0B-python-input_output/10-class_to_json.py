#!/usr/bin/python3
"""
This is the "class_to_json" module.
This module contains function, class_to_json().
"""


def class_to_json(obj):
    """ Returns the dict description for JSON serialization of an object."""
    return vars(obj)
