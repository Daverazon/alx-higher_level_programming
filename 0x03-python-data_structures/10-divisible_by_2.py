#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    return(list(True if (x % 2 == 0) else False for x in my_list))
