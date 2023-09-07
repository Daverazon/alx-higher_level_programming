#!/usr/bin/python3
from sys import argv
if (__name__ == "__main__"):
    sum = 0
    for args in argv:
        if (args == argv[0]):
            continue
        sum += int(args)
    print(sum)
