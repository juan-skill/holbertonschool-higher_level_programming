#!/usr/bin/python3


def no_c(str):

    n_str = ''
    for i in str:
        if i != 'c' and i != 'C':
            n_str += i

    return n_str
