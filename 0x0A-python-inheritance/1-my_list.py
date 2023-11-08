#!/usr/bin/python3

"""
This module contains a child class with a mehtod that
prints sorted list in ascending order.
"""


class MyList(list):
    """ This class inherits from the list class.

    Args:
        list: list class

    """

    def print_sorted(self):
        """ Method that print sorted list """
        tmp = self.copy()
        tmp.sort()
        print(tmp)
