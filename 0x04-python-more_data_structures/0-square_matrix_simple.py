#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mtx = [[i**2 for i in matrix[j]] for j in range(len(matrix))]
    return(mtx)
