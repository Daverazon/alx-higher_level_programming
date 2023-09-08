#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        r = len(row)
        for column in row:
            print("{}".format(column), end='')
            if (r > 1):
                print(" ", end='')
            r -= 1
        print()
