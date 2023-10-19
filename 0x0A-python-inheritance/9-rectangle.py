#!/usr/bin/python3
'''Defines a rectangle class that inherits from the BaseGeometry class'''


class BaseGeometry:
    '''Represent a BaseGeometry class'''
    def area(self):
        '''Raises an exception'''
        raise Exception("area() not implemented")

    def integer_validator(self, name, value):
        '''Validates type and value of the argument "value".'''
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    '''Represent a rectangle class'''

    def __init__(self, width, height):
        '''Initialize a BaseGeometry class'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''returns area of a rectangle'''
        return self.__width * self.__height

    def __str__(self):
        """prints informal representation of object"""
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
