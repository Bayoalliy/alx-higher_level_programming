#!/usr/bin/python3

"""

This is a class that prevents user from 
dynamically creating new instances attributes.

"""

class LockedClass:
    __slots__ = ["first_name"]

    def __init__(self):
        """ constructor function """
        pass
