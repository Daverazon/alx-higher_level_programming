#!/usr/bin/python3
'''Defines an inheritance checker function'''


def inherits_from(obj, a_class):
    '''returns True if the object is an instance
    of a class that inherited (directly or indirectly) from the specified class
    otherwise False'''
    if (isinstance(obj, a_class) and a_class is not type(obj)):
        return True
    return False
