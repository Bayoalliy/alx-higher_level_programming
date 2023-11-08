#!/usr/bin/python3

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
