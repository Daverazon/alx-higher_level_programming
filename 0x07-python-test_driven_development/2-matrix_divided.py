#!/usr/bin/python3
'''
Define a matrix element dividing function
>>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
'''


def matrix_divided(matrix, div):
    '''Divide all elements of a function

    Args:
        matrix (list): a list of lists
        div (int/float): divisor number
    Returns:
        (list): new matrix containing divided elements
    '''
    if div == 0:
        raise ZeroDivisionError('division by zero')
    elif type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    elif not (all(isinstance(row, list) for row in matrix) and
              all((all(isinstance(x, int) or isinstance(x, float)
                       for x in row)) for row in matrix)):
        raise TypeError('matrix must be a matrix (list of lists)'
                        ' of integers/floats')
    elif not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')
    else:
        new = [list(map(lambda x, div=div: round(x/div, 2), row)) for row
               in matrix]
        return new
