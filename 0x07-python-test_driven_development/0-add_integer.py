#!/usr/bin/python3
'''Define an addition function'''


def add_integer(a, b=98):
    '''Add two numbers
    
    Examples:
        >>> add_integer(5)
        103
    Args:
        a (int): first number
        b (int): second number 
    Returns:
        int: sum of the two numbers
    '''
    if not(isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    else:
        a = int(a)
    if not(isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    else:
        b = int(b)

    return a + b