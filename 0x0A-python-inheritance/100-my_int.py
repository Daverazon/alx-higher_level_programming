#!/usr/bin/python3
'''Define a MyInt class'''


class MyInt(int):
    '''Represents MyInt, a rebel of int'''
    def __eq__(self, __value: object) -> bool:
        '''Inverts the != operator'''
        return super().__ne__(__value)
    
    def __ne__(self, __value: object) -> bool:
        '''Inverts the != operator'''
        return super().__eq__(__value)
