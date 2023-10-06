#!/usr/bin/python3
'''Define a square'''


class Square:
    '''Represent a square'''

    def __init__(self, size=0):
        '''initialise a new square

        Args:
            size (int): size of a square
        '''

        self.__size = size

    @property
    def size(self):
        '''Check if size is correct type and value'''

        if type(self.__size) is not int:
            raise TypeError("Size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    check_size()
