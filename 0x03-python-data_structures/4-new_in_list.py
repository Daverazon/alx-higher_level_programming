i#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = my_list[:]
    if (idx < len(my_list) and idx > -1):
        copy[idx] = element
    return (copy)
