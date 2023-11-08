#!/usr/bin/python3

"""
This module contains a function that checks if an
object is an instance of the child of the specified class

"""


def inherits_from(obj, a_class):
    """ function that returns true if an object is
        a child instance of a specified class.
    """
    if (type(obj) is a_class):
        return False
    return (isinstance(obj, a_class))
