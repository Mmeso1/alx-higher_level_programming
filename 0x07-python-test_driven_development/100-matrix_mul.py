#!/usr/bin/python3

""" Validate matrix """


def validate_matrix(matrix, name):
    if not isinstance(matrix, list):
        raise TypeError(f"{name} must be a list")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(f"{name} must be a list of lists")

    if matrix == [] or matrix == [[]]:
        raise ValueError(f"{name} can't be empty")

    if any(
            not all(isinstance(element, (float, int))for element in row)
            for row in matrix
            ):
        raise TypeError(f"{name} should contain only integers or floats")

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError(f"each row of {name} must be of the same size")


""" Matrix multiplication """


def matrix_mul(m_a, m_b):
    """ To multiply matrixes """

    validate_matrix(m_a, "m_a")
    validate_matrix(m_b, "m_b")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
