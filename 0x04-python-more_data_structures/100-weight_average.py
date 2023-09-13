#!/usr/bin/python3
def weight_average(my_list=[]):
    add, div = 0, 0
    if my_list:
        mul = [x * y for x, y in my_list]
        for row in my_list:
            div += row[1]
        for m in mul:
            add += m
    return add / div
