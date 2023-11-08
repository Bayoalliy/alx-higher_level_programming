#!/usr/bin/python3

"""
This module contains a function that checks if an
object is exactly an instance of the specified class
or if the object is an instance of a class that
inherited from the specified class.

"""


def is_kind_of_class(obj, a_class):
    """ function that returns true if an object is
        an instance or child instance of a specified class.
    """
    return (isinstance(obj, a_class))
