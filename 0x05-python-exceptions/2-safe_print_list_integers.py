#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    num = 0
    try:
        for i in range(x):
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end='')
                num += 1
        print('')
        return num
    except ValueError:
        print('')
        return num
