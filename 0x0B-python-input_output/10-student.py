#!/usr/bin/python3
'''Define a Student class'''


class Student:
    def __init__(self, first_name, last_name, age):
        """Initialise a Student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''retrieve a dictionary representation of a Student instance'''
        if attrs:
            specific_attr = {}
            for attr in attrs:
                if attr in vars(self):
                    specific_attr[attr] = getattr(self, attr)
        else:
            specific_attr = self.__dict__
        return specific_attr
