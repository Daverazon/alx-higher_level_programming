#!/usr/bin/python3
'''Define a Square'''


class Square:
    '''Represent a square'''

    def __init__(self, size=0):
        '''Initialize a new square

        Args:
            size (int): size of the new square'''

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''Calculate current area of square

        Returns:
            current area of square'''
        return self.__size ** 2
