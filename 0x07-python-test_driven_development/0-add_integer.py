#!/usr/bin/python3

"""
Returns the addition of two arguments
>>>add_integer(2, 3)
5
    """

def add_integer(a, b=98):
    """A function that adds two integers

    Args:
        a (int): The first number to be added
        b (int, optional): The second number to be added. Defaults to 98.

    Raises:
        TypeError: a must be an integer
        TypeError: b must be an integer

    Returns:
        int: Addition of a and b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')

    add = int(a) + int(b)
    return add
