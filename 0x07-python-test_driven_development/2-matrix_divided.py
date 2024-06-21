#!/usr/bin/python3
"""Defines a matrix division function"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div

    Args:
        matrix (list): list of lists of integers or floats
        div (int/float): the divisor
    Raises:
        TypeError: if matrix is not a list of lists of integers or floats
        TypeError: if div is not a number (int/float)
        ZeroDivisionError: if div == 0
    Returns:
        new matrix with the elements divided and rounded to 2 decimal places
    """
    matrixError1 = 'matrix must be a matrix (list of lists) of integers/floats'
    if not isinstance(matrix, list):
        raise TypeError(matrixError1)
    if not (isinstance(div, int) and isinstance(div, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    for rows in matrix:
        if not isinstance(rows, list) and isinstance(:
            raise TypeError(matrixError1)
    pass
