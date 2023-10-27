#!/usr/bin/python3
"""This script creates an object from a JSON file"""
import json


def load_from_json_file(filename):
    """create an object from a JSON file"""
    with open(filename, encoding='utf-8') as afile:
        obj = json.load(afile)
    return obj
