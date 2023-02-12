#!/usr/bin/python3
"""
contains a function, matrix_divided
"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix"""
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    count = None
    for i in matrix:
        if count is None:
            count = len(i)
        if type(i) is not list:
            raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
        if len(i) != count:
            raise TypeError("Each row of the matrix must have the same sizes")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by Zero")
    return [[round(l/div, 2) for l in j] for j in matrix]
