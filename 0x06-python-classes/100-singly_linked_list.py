#!/usr/bin/python3
'''Define a Node'''


class Node:
    '''Represent the node of a singly linked list'''

    def __init__(self, data, next_node=None):
        '''intialize a new node'''

        self.__data = data
        self.__next_node = next_node
