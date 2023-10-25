#!/usr/bin/python3
'''This module creates a function that appends a string to a text file'''


def append_write(filename="", text=""):
    '''Appends a string at the end of a text file and return number
    of characters added'''
    with open(filename, 'a', encoding='UTF-8') as f:
        return f.write(text)
