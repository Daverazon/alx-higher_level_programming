#!/usr/bin/python3
'''Define a square'''


class Square:
    '''Represent a square'''

    def __init__(self, size=0):
        '''Initialuze a new square

        Args:
            size (int): size of the square
        '''

        self.size = size

    @property
    def size(self):
        '''get the size

        Returns:
            Size of the square'''

        return self.__size

    @size.setter
    def size(self, value):
        '''set the value of size

        Args:
            value (int): new value for size
        '''

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Calculate the area of a square

        Returns:
            current area of square'''
        return self.__size ** 2
