#!/usr/bin/python3
""" In this module, a class `Square` is created.
the class checks if the size attr is positive and integer.
"""


class Square:
    """ This is a class defining a square.
        Args:
            size (int): the size of the square.
    """
    def __init__(self, size=0):
        self._Square__size = size
        if int(size) != size:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        return(self._Square__size)

    @size.setter
    def size(self, value):
        self._Square__size = value
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ A public instance method that calculates the area of a square
        """
        return(self._Square__size**2)
