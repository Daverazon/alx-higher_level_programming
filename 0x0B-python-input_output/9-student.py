#!/usr/bin/python3
'''Define a Student class'''


class Student:
    def __init__(self, first_name, last_name, age):
        """Initialise a Student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''retrieve a dictionary representation of a Student instance'''
        return (vars(self))  # or self.__dict__
