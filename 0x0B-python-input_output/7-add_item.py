#!/usr/bin/python3
"""This  script that adds all arguments to a
Python list, and then save them to a file"""
import json
import sys
save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file


def add_arguments_to_json_file(filename):
    """This  script that adds all arguments to a
Python list, and then save them to a file"""
    try:
        exist = open(filename)
    except FileNotFoundError:
        new = open(filename, 'w')
        new.close()
    else:
        exist.close()

    lis = load(filename)
    print(type(lis))
    index = 1
    while (index < len(sys.argv)):
        lis.append(sys.argv[index])
        index += 1

    save(lis, filename)


def main():
    """main function"""
    add_arguments_to_json_file("add_item.json")


main()
