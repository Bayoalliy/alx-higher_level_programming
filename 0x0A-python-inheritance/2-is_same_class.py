#!/usr/bin/python3

"""
This module contains a function that checks if an
object is exactly an instance of the specified class

"""


def is_same_class(obj, a_class):
    """ function that returns true if an object is
        an instance of a specified class.
    """
    return (type(obj) is a_class)
