#!/usr/bin/python3

"""Write a class Square that defines a square by: (based on 3-square.py)
    """


class Square:
    """Attributes:
            size: privates class that hold the square size

        """
    def __init__(self, size=0, position=(0, 0)):
        """initializes the  size

        Args:
            size (int, optional): size. Defaults to 0.
        """

        self._Square__size = size
        self.position = position

    @property
    def size(self):
        """ A method that returns the size of square

        Returns:
            int: size of square
        """
        return self._Square__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = value

    def area(self):
        """Returns the area of square

        Returns:
            int: area
        """
        return self._Square__size * self._Square__size

    @property
    def position(self):
        """ returns the position

        Returns:
            int: position
        """
        return self.position

    def my_print(self):
        """ Prints the square
        """
        sz = self._Square__size
        if sz == 0:
            print('')
        for i in range(sz):
            print("#" * sz)
