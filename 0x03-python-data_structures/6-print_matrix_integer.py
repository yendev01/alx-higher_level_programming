#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        length = len(i)
        for j in range(length - 1):
            print("{:d}".format(i[j]), end=" ")
        if length > 0:
            print("{}".format(i[length - 1]))
        else:
            print()
