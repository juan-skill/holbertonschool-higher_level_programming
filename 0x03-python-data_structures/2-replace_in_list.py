#!/usr/bin/python3


def replace_in_list(list, idx, element):

    if idx > (len(list) - 1) or idx < 0:
        return list

    list[idx] = element

    return list
