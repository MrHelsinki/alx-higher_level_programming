#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    def parser(list=[]):
        cp = []
        for i in list:
            cp.append(i ** 2)
        return cp
    square_matrix = list(map(parser, matrix))
    return square_matrix
