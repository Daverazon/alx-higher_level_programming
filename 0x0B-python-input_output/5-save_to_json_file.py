#!/usr/bin/python3
"""This module defines a function that writes an Object to
a text file, using JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """write an Object to a text file, using JSON
     representation"""
    with open(filename, 'w', encoding='utf-8')as afile:
        afile.write(json.dumps(my_obj))
