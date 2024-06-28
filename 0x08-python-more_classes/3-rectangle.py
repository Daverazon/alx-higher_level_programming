#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """
    Defines a rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        if self.width > 0 and self.height > 0:
            return '\n'.join(['#' * self.width for row in range(self.height)])
        return ''

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height

    def area(self):
        """
        calculate the area of the rectangle

        Usage:
            self.area()
        Args:
            none
        Returns:
            area of the rectangle object
        """
        return self.height * self.width

    def perimeter(self):
        """
        calculate the perimeter of the rectangle

        Usage:
            self.perimeter()
        Returns:
            perimeter of the rectangle object
        """
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)
