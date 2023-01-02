#!/usr/bin/python3
""" In this module, a class `Square` is created
    to demonstrate how private attributes work."""


class Square:
    """ This is a class defining a square.
        Args:
            size (int): the size of the square.
    """
    def __init__(self, size):
        self._size = size
