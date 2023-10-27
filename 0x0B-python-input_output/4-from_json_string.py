#!/usr/bin/python3
"""This module defines a function that returns an object (python
 data structure) represented by a JSON string"""
import json


def from_json_string(my_str):
    ''' Return an object (python data structure) represented by a
    JSON string'''
    return (json.loads(my_str))
