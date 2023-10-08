#!/usr/bin/python3

class Square:
    '''Define a square'''

    def __init__(self, size=0):
        '''Represent a square

        Args:
            size (int): size of the square
        '''

        self.size = size

    @property
    def size(self):
        '''get the value of size

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

    def my_print(self):
        '''prints the square with #'''

        for row in range(self.__size):
            for column in range(self.__size):
                print("#", end='')
            print()

        if self.__size == 0:
            print()
