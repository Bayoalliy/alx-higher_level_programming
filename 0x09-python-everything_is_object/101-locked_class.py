#!/usr/bin/python3

"""

This is a module that prevents user from
dynamically creating new instances attributes.


"""


class LockedClass:
    """ main class of the module """
    __slots__ = ["first_name"]

    def __init__(self):
        """ constructor function """
        pass
