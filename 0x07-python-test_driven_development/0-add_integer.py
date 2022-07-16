#!/usr/bin/python3

"""
Returns the addition of two arguments
>>>add_integer(2, 3)
5
    """


def add_integer(a, b=98):
    """A function that adds two integers
    Returns (int): Addition of a and b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    add = a + b
    return add
