#!/usr/bin/python3
def no_c(my_string):
    lis = list(my_string)
    for c in lis:
        if (c == "c" or c == "C"):
            lis.remove(c)
    return ("".join(lis))
