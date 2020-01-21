#!/usr/bin/python3
"""
This is the "my list" module.
The my list module contains  one function, print_sorted().
"""


class MyList(list):
    """Represents a MyList, subclase."""

    def print_sorted(self):
        """Print the list in ascending sort."""
        print(sorted(self))
