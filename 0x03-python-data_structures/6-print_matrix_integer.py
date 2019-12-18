#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    str = ''
    for row in matrix:

        str += '\n'
        for col in row:
            str += "{:d} ".format(col)
        str = str[:-1]

    print(str[1:])
