#!/usr/bin/python3
from models.base import Base

"""
This module contains a Rectangle class that is a child of Base.
"""


class Rectangle(Base):
    """ Rectangle class inheriting from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ constrctor function """
        Base.__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        @property
        def width(self):
            """ width getter """
            return self.__width

        @width.setter
        def width(self, a):
            """ width setter """
            self.__width = a

        @property
        def height(self):
            """height getter"""
            return self.__height

        @height.setter
        def height(self, a):
            """ height setter """
            self.__height = a

        @property
        def x(self):
            """ x getter """
            return x.__width

        @x.setter
        def x(self, a):
            """ x setter """
            self.__x = a

        @property
        def y(self):
            """ y getter """
            return self.__y

        @y.setter
        def y(self, a):
            """ y setter"""
            self.__y = a
