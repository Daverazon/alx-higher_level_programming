#!/usr/bin/python3
"""This script defines python to json representing function"""


def class_to_json(obj):
    """ returns the dictionary description with simple data
    structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object"""
    json_serialisable = obj.__dict__  # or vars(obj)
    return json_serialisable
