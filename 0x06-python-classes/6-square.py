#!/usr/bin/python3
""" In this module, a class `Square` is created.
the class checks if the size attr is positive and integer.
"""


class Square:
    """ This is a class defining a square.
        Args:
            size (int): the size of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        self._Square__size = size
        if int(size) != size:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self._Square__position = position
        if type(position) != tuple and len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")

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

    @property
    def position(self):
        return(self._Square__position)

    @position.setter
    def position(self, value):
        self._Square__position = value
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")

        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        if self._Square__size == 0:
            print()

        if self._Square__position[1] != 0:
            print("" * self._Square__position[1])

        for i in range(self._Square__size):
            print(" " * self._Square__position[0], end="")
            for j in range(self._Square__size):
                print("#", end="")
            print()

    def area(self):
        """ A public instance method that calculates the area of a square
        """
        return(self._Square__size**2)
