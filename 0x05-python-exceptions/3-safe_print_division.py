#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        ret = a / b
        return ret
    except ZeroDivisionError:
        ret = None
        return ret
    finally:
        print("Inside result: {}".format(ret))
