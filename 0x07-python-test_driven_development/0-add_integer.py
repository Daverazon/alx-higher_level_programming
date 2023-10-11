#!/usr/bin/python3
'''Define an addition function

>>> add_integer(5, 10)
15
'''


def add_integer(a, b=98):
    '''
    Add two numbers
    '''
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    else:
        a = int(a)
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    else:
        b = int(b)

    return a + b