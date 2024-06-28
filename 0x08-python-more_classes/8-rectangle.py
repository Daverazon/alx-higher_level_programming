#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """
    Defines a rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.__class__.number_of_instances += 1
        self.width = width
        self.height = height

    def __str__(self):
        if self.width > 0 and self.height > 0:
            return '\n'.join([str(self.print_symbol) * self.width for
                             row in range(self.height)])
        return ''

    def __repr__(self):
        return f"{self.__class__.__name__}({self.width}, {self.height})"

    def __del__(self):
        self.__class__.number_of_instances -= 1
        print('Bye rectangle...')

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare rectangle areas to get the biggest

        Usage:
            bigger_or_equal(rect_1, rect_2)
        Args:
            rect_1 (Rectangle): first Rectangle object
            rect_2 (Rectangle): second Rectangle object
        Raises:
            TypeError: if the objects are not Rectangles
        Returns:
            The biggest rectangle object based on area or the first one if\
                    both have the same area
        """
        for obj in ((rect_1, 'rect_1'), (rect_2, 'rect_2')):
            if not isinstance(obj[0], Rectangle):
                raise TypeError(f'{obj[1]} must be an instance of Rectangle')
        if rect_1.area() > rect_2.area() or rect_1.area() == rect_2.area():
            return rect_1
        return rect_2
