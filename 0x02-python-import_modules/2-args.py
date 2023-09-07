#!/usr/bin/python3
from sys import argv
if (__name__ == "__main__"):
    num = len(argv) - 1
    if (num == 1):
        print("{} argument:".format(num))
        print("{}: {}".format(num, argv[num]))
    elif (num == 0):
        print("{} arguments.".format(num))
    else:
        print("{} arguments:".format(num))
        num = 1
        while num < len(argv):
            print("{}: {}".format(num, argv[num]))
            num += 1
