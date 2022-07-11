#!/usr/bin/python3

"""A class Square that defines a square by: (based on 2-square.py)
    """


class Square:
    """Attributes:
            size: privates class that hold the square size

        """
    def __init__(self, size=0):
        """_summary_

        Args:
            size (int, optional): size. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = size

    def area(self):
        return self._Square__size * self._Square__size
