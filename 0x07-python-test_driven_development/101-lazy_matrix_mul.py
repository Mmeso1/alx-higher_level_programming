import numpy as np

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


""" Lazy matrix multiplication """


def lazy_matrix_mul(m_a, m_b):
    """ using numPy to multily matrices """
    validate_matrix(m_a, "m_b")
    validate_matrix(m_b, "m_b")

    np_m_a = np.array(m_a)
    np_m_b = np.array(m_b)

    return (np_m_a @ np_m_b).tolist()

