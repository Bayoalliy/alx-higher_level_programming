#!/usr/bin/python3

"""
This module define a class named square that inherits from
Rectangle class.

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ The square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ constructor function """
        Rectangle.__init__(self, size, size, x, y, id)

    def __str__(self):
        """ overriding the inbuilt __str__ function """
        str1 = "[Square] ({}) {}/{} ".format(self.id, self.x, self.y)
        str2 = "- {}".format(self.width)
        return str1 + str2
