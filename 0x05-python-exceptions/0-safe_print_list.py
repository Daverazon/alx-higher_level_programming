#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    index = 0
    while index < x:
        try:
            print("{}".format(my_list[index]), end='')
        except IndexError:
           break
        else:
           index += 1
    if index > 0: 
        print()
    return (index)   
