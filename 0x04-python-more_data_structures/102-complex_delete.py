#!/usr/bin/python3


def complex_delete(a_dictionary, value):

    copy = a_dictionary.copy()

    for i in copy:
        if a_dictionary[i] == value:
            del a_dictionary[i]

    return a_dictionary
