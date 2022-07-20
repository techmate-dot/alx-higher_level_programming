#!/usr/bin/python3

""" Write a function that divides all
elements of a matrix.
"""


def check_type(matrix, div):
    """returns a boolean

    Args:
        matrix (any): any value

    Raises:
        TypeError: if it is not  A LIST OF LIST
        TypeError: if it is not a float or int

    Returns:
        bool: true if it is a list of list otherwise returns false
    """
    value = True
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) and not isinstance(matrix[0], list):
        value = False
        raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
    for row in matrix:
        for element in row:
            if not isinstance(element, int) and not isinstance(element, int):
                value = False
                raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
    return value


def matrix_divided(matrix, div):
    """Divides the element of a matrix by div

    Args:
        matrix (list): list of lists
        div (int): intteger that divides the matrix

    Raises:
        ZeroDivisionError: raised when div is zero
        TypeError: raise when length of the rows are different

    Returns:
        list: divided list of lists(matrix)
    """
    check = check_type(matrix, div)
    length = len(matrix[0])
    new_matrix = []
    new_row = []
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if length != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        length = len(row)
    if check is True:
        for row in matrix:
            for element in row:
                new_row.append(round((element / div), 2))
            new_matrix.append(new_row)
    return new_matrix
