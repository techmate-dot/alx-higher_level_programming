#!/bin/usr/python3

def safe_print_division(a, b):
    try:
        ret = None
        ret = a / b
        return ret
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: ", end='')
        print("{}".format(ret))
