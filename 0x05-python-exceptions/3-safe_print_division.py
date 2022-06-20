#!/bin/usr/python3

def safe_print_division(a, b):
    ret = None
    try:
        ret = a / b
        return ret
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(ret))
