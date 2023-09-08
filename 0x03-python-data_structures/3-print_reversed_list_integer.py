#!/usr/bin/bash
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for rev in my_list:
        print("{}".format(rev))
