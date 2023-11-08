#!/usr/bin/python3

"""
This module contains a function that produces a
list of attribute and method of an object.
"""


def lookup(obj):
    """
    This function returns the list of available
    attributes and methods of an object.

    Args:
        obj: any pytonic object.

    Returns:
        List of atrributes of obj.
    """

    return (dir(obj))
