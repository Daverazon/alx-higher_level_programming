#!/usr/bin/python3
'''Define a square'''


class Square:
    '''Represent a square'''

    def __init__(self, size=0):
        '''initialise a new square

        Args:
            size (int): size of a square
        '''

        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
