#!/usr/bin/python3
'''Define a rectangle'''


class Rectangle:
    '''Represent a rectangle'''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''Initialize a new rectangle'''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        return 2 * (self.__width + self.__height)

    def __str__(self):
        '''return printable representation of object'''
        rectangle_str = ''
        if self.__width == 0:
            return rectangle_str
        for row in range(self.__height):
            rectangle_str += str(self.print_symbol) * self.__width
            if not row == self.__height - 1:
                rectangle_str += '\n'
        return rectangle_str

    def __repr__(self):
        '''string representation of the rectangle to be able to recreate a
         new instance by using eval()'''
        return '{}({}, {})'.format(
            self.__class__.__name__, self.__width, self.__height)

    def __del__(self):
        '''destroy/delete the rectangle'''
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
