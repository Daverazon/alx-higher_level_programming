#!/usr/bin/python3
'''This module creates a function that reads a text file'''


def read_file(filename=""):
    """Reads a text file and prints it to stdout"""
    with open(filename, encoding='UTF-8') as f:
        print(f.read())
