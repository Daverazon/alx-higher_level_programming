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

    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not isinstance(matrix, list) or matrix in ([], [[]]):
        raise TypeError(matrixError1)
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(matrixError1)

    #  create a deepcopy loop
    mCopy = [row[:] for row in matrix]

    row = 0
    size = len(mCopy[row])
    while row < len(mCopy):
        if len(mCopy[row]) != size:
            raise TypeError("Each row of the matrix must have the same size")

        column = 0
        while column < len(mCopy[row]):
            number = mCopy[row][column]
            if not (isinstance(number, int) or isinstance(number, float)):
                raise TypeError(matrixError1)
            mCopy[row][column] = round(mCopy[row][column]/div, 2)
            column += 1
        row += 1
    return mCopy
