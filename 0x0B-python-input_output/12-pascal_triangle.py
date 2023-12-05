#!/usr/bin/python3

""" Pascal's Triangle """

def pascal_triangle(n):
    """ The pascal's triangle """
    if n <= 0:
        return []
    else:
        triangle = []
        for i in range(num_rows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)
        return triangle