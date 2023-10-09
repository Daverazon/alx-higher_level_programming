#!/usr/bin/python3
'''Define a square'''


class Square:
    '''Represent a square'''

    def __init__(self, size=0, position=(0, 0)):
        '''Initialize a new square

        Args:
            size (int): size of the square
            position (tuple): position of the square
        '''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''get size

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

    @property
    def position(self):
        '''get the position of the square

        Returns:
            position of the square'''
        return self.__position

    @position.setter
    def position(self, value):
        '''set the value of position

        Args:
            value (tuple): new value for position
        '''
        if not isinstance(value, tuple) or len(value) != 2 or not\
           all(isinstance(x, int) for x in value) or not\
           all(x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive intgers")
        self.__position = value

    def area(self):
        '''Calculate the area of a square

        Returns:
            current area of square'''
        return self.__size ** 2

    def my_print(self):
        '''prints the square with #'''
        if self.__size == 0:
            print("")
            return
        for prow in range(self.__position[1]):
            print("")
        for row in range(self.__size):
            for pcolumn in range(self.__position[0]):
                print(" ", end='')
            for column in range(self.__size):
                print("#", end='')
            print("")
