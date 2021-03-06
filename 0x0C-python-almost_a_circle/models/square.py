#!/usr/bin/python3
"""a class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """__init__ method of class Square
        Args:
            size (int): size of square side
            x (int): x-coordinate of Square
            y (int): y-coordinate of Square
            id (int): id of Square object
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of square object"""
        return "[{}] ({:d}) {:d}/{:d} - {:d}".format(
            type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """size getter method for Square"""
        return self.width

    @size.setter
    def size(self, size):
        """Setter method for Square size
        Args:
            size (int): size of square side
        Raises:
            TypeError: if `size` is not an integer
            ValueError: if `size` is not greater than zero
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update attributes
        Args:
            args: arguments
            kwargs: key-word arguments
        """
        if len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
        elif len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                if k == 'size':
                    self.size = v
                if k == 'x':
                    self.x = v
                if k == 'y':
                    self.y = v

    def to_dictionary(self):
        """Dictionary representation of object
        Returns:
            dictionary of attributes
        """
        obj_dict = {}
        for attr in ['id', 'size', 'x', 'y']:
            obj_dict[attr] = getattr(self, attr)
        return obj_dict
