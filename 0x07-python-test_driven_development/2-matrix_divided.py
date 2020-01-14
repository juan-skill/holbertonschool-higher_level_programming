#!/usr/bin/python3
"""
Matrix Divided module
Has a function to divide matrixes by a integer or a float
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.
    All elements will be divided by div and rounded to 2 decimal places.
    Returns new matrix.
    """

    if matrix is None or \
       len(matrix) is 0 or\
       len(matrix[0]) is 0:
        raise TypeError('''matrix must be a matrix (list of lists)
        of integers/floats''')

    new_matrix = []
    msg_type = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")

    try:
        for count, row in enumerate(matrix):

            if not isinstance(row, list):
                raise TypeError(msg_type)

            if len(row) != len(matrix[0]):
                raise TypeError(msg_type)

            new_matrix.append(row[:])
            for val, item in enumerate(row):

                if not isinstance(item, (int, float)):
                    raise TypeError(msg_type)
                new_matrix[count][val] = round(item / div, 2)
    except:
        raise
    else:
        return new_matrix
