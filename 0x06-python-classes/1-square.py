#!/usr/bin/python3
'''Define a square class'''


class Square:
    """Represent a square"""

    def __init__(self, size):
        '''Initialise a new square

        Args:
            size (int): the size of the square
        '''

        self.__size = size
