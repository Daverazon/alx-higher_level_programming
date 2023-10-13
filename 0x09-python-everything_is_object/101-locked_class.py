#!/usr/bin/python3
'''This module defines a LockedClass'''


class LockedClass:
    '''Represent a LockedClass

    Note:
        user can only dynamically create new instance attribute
        if it is called `first_name`.'''
    __slots__ = ("first_name", )

    def __init__(self, first_name=None):
        '''Initialize a LockedClass'''
        self.first_name = first_name
