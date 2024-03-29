#!/usr/bin/python3

"""
This module define a class that will be the base of all other
classes in this project The goal of it is to manage id attribute
in all your future classes and to avoid duplicating
the same code (by extension, same bugs)

"""


class Base:
    """ The base class for all other classes """
    __nb_objects = 0

    def __init__(self, id=None):
        """ constrctor fuction """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
