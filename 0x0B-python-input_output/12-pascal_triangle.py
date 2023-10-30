#!/usr/bin/python3
'''This module defines a pascal triangle function'''


def pascal_triangle(n):
    '''return a list of lists of integers representing the
      Pascal's triangle of n'''
    pt = []
    if n <= 0:
        return pt
