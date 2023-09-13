#!/usr/bin/python3
def weight_average(my_list=[]):
    average, add, div = 0, 0, 0
    if my_list:
        mul = [x * y for x, y in my_list]
        for row in my_list:
            div += row[1]
        for m in mul:
            add += m
        average = add / div
    return average
