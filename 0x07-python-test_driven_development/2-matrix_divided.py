#!/usr/bin/python3

""" Divide a matrix """

def matrix_divided(matrix, div):
    """
     divides all elements of a matrix.
    """
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if type(matrix) is not list:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    
    """ Checking the individual values of the matrix """

    matrix_len = len(matrix[0])
    new_matrix = []

    for i in range(len(matrix)):
        if len(matrix[i]) != matrix_len:
            raise TypeError('Each row of the matrix must have the same size')

        row = []
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) not in [int, float]:
                raise TypeError(
                        'matrix must be a matrix (list of lists) of integers/floats')
            else:
                row.append(round(float(matrix[i][j]) / div, 2))
        new_matrix.append(row)
    return new_matrix
