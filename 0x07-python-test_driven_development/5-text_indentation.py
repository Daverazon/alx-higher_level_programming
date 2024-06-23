#!/usr/bin/python3
"""Defines a text indentation function"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and : without leaving any space at the beginning or at the end of each printed line

    Usage:
        text_indentation(text)
    Args:
        text (str)
    Raises:
        TypeError: if text is not a string
    Returns:
        None
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

