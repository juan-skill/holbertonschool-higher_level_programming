#!/usr/bin/python3


def max_integer(list=[]):

    if len(list) <= 0 or list is None:
        return None

    max = list[0]
    for item in list:
        if item > max:
            max = item

    return max
