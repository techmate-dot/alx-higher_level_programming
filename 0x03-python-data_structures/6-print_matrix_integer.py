#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        last = len(row)
        for num in row:
            last -= 1
            if last == 0:
                print("{:d}".format(num))
            else:
                print("{:d}".format(num), end=' ')
