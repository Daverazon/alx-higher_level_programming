#!/usr/bin/python3
"""This module defines a class that inherits from 'list'"""


class MyList(list):
    """Represent a derived class of list"""
    def print_sorted(self):
        """Print the list, but in ascending sorted order"""
        new = MyList()
        new = self[:]
        new.sort()
        print(new)
