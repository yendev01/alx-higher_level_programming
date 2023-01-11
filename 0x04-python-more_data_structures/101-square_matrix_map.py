#!/usr/bin
def square_matrix_map(matrix=[]):
    return list(map(lambda x	:	list(map(lambda i	:	x[i]*x[i],
                    range(len(matrix)))), matrix))
