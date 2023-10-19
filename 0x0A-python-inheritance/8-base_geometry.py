#!/usr/bin/python3
'''Defines a BaseGeometry class'''


class BaseGeometry:
    '''Represent a BaseGeometry class'''
    def area(self):
        '''Raises an exception'''
        raise Exception("area() not implemented")

    def integer_validator(self, name, value):
        '''Validates type and value of the argument "value".'''
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name must be greater than 0")
