#!/usr/bin/python3
"""Defines an integer addition function"""


def add_integer(a, b=98):
    """
    Returns the integer sum of two values

    Float arguments are first casted to integers
    """
    ab = (['a', a], ['b', b])
    for x in ab:
        if not (isinstance(x[1], int) or isinstance(x[1], float)):
            raise TypeError(f'{x[0]} must be an integer')

        if isinstance(x[1], float):
            x[1] = int(x[1])

    return ab[0][1] + ab[1][1]
