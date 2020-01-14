#!/usr/bin/python3
"""
   This module prints text with indentation
   This module contains the following functions: text_indentation
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after these characters: <<.>> <<?>> <<:>>:
    """
    if text is None or not isinstance(text, str) or len(text) < 0:
        raise TypeError("text must be a string")

    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n').replace(':', ':\n\n')

    print("\n".join(list(l.strip() for l in text.split('\n'))), end="")
