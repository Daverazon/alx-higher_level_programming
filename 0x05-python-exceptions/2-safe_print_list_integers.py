#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    index, invalid = 0, 0
    while index < x:
        try:
            print("{:d}".format(my_list[index]), end='')
        except (TypeError, ValueError):
            invalid += 1
        index += 1
    index -= invalid
    print()
    return (index)
