#!/usr/bin/python3


def print_reversed_list_integer(list=[]):

    if list is not None and len(list) > 0:
        j = len(list) - 1

        for item in list:
            print("{:d}".format(list[j]))
            j -= 1
