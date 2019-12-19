#!/usr/bin/python3


def multiply_by_2(a_dictionary):

    n_dictionary = {}

    for key, value in a_dictionary.items():
        n_dictionary[key] = value * 2

    return n_dictionary
