#!/usr/bin/python3
"""Defines a function that prints a square with the # character"""


def print_square(size):
    """
    prints a square with the character #

    Usage:
        print_square(size)
    Args:
        size (int): length of the square
    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than zero
        TypeError: if size is a float and is less than zero
    Returns:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for column in range(size):
            print("#", end="")
        print("")
