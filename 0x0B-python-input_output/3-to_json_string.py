#!/usr/bin/python3
"""This module defines a function that returns JSON representation of object"""
import json


def to_json_string(my_obj):
    ''' Return the JSON representation of an object (string)'''
    return (json.dumps(my_obj))
