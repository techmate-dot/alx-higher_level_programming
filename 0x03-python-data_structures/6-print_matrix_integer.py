#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) == 0:
        print("")
    for row in matrix:
        last = len(row)
        for num in row:
            last -= 1
            if last == 0:
                print("{:d}".format(num))
            else:
                print("{:d}".format(num), end=' ')
