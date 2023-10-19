#!/usr/bin/python3
'''Defines a BaseGeometry class'''


class BaseGeometry:
    '''Represent a BaseGeometry class'''
    def area(self):
        '''Raises an exception'''
        raise Exception("area() not implemented")

    def integer_validator(self, name, value):
        '''Validates type and value of the argument "value".'''
        if type(value) != int :
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
