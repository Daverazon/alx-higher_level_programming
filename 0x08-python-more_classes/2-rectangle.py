#!/usr/bin/python3
'''Define a rectangle'''


class Rectangle:
    '''Represent a rectangle'''
    def __init__(self, width=0, height=0):
        '''Initialize a new rectangle'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''get/set for width of rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        '''get/set for heigtht of rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        '''return the area of the rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''return the perimeter of the rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
