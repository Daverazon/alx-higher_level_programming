#!/usr/bin/python3
'''Defines a square printing function'''


def print_square(size):
    '''Prints a square with the character #'''

    if not isinstance(size, int) or isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    else:
        for row in range(size):
            for column in range(size):
                print('#', end='')
            print('')
