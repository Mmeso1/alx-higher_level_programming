#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squared_row = []
    if len(matrix) > 0:
        for row in matrix:
            squared_row.append(list(map(lambda i: i**2, row)))
        return squared_row
