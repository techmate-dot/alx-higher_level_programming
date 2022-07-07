#!/usr/bin/python3
"""Function that computes and returns the Pascal's Triangle of n"""


def pascal_triangle(n):
    """Pascal triangle
    Args:
        n (int): number of rows
    Returns:
        matrix representing Pascal's triangle
    """
    matrix = []
    if n <= 0:
        return matrix
    else:
        for r in range(n):
            if r == 0:
                matrix.append([1])
            elif r == 1:
                matrix.append([1, 1])
            else:
                matrix.append([1 for x in range(r + 1)])
                for c in range(1, len(matrix[r]) - 1):
                    matrix[r][c] = matrix[r - 1][c - 1] + matrix[r - 1][c]

    return matrix
