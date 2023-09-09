#!/usr/bin/python3
def max_integer(my_list=[]):
    if (len(my_list) > 0):
        current_big = 0
        for big in my_list:
            if (big > current_big):
                current_big = big
    return (current_big)
