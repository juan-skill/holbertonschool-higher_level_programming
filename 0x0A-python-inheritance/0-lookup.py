#!/usr/bin/python3
"""
This is the module lookup module
This module supplies, lookup().
"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object."""
    return dir(obj)
