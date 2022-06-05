#!/usr/bin/python3
def print_list_integer(my_list=[]):
    str = '{:d}'
    for i in range(len(str) + 1):
        print(str.format(my_list[i]))
