#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if (idx < len(my_list) and idx > -1):
        for lis in my_list:
            if (my_list.index(lis) == idx):
                my_list.remove(lis)
    return (my_list)
