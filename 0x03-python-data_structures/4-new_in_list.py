#!/usr/bin/python3


def new_in_list(list, idx, element):

    if list is None or idx >= len(list) or idx < 0:
        return list

    newlist = list[:]
    newlist[idx] = element

    return newlist
