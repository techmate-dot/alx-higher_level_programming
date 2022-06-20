#!/bin/usr/python3

def safe_print_division(a, b):
    try:
        ret = a / b
        return ret
    except ZeroDivisionError:
        ret = None
        return None
    finally:
        print("Inside result: ", end='')
        print("{}".format(ret))
