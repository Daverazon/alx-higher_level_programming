#!/usr/bin/python3
def no_c(my_string):
    lis = []
    for c in my_string:
        if (c != "c" or c != "C"):
            lis.append(c)
    return ("".join(lis))
