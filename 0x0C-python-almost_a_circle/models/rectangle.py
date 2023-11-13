#!/usr/bin/python3
from models.base import Base

"""
This module contains a Rectangle class that is a child of Base.
"""


class Rectangle(Base):
    """ Rectangle class inheriting from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ constrctor function """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, val):
        """ width setter """
        if not type(val) is int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, a):
        """ height setter """
        if not type(a) is int:
            raise TypeError("height must be an integer")
        elif a <= 0:
            raise ValueError("height must be > 0")
        self.__height = a

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, a):
        """ x setter """
        if not type(a) is int:
            raise TypeError("x must be an integer")
        elif a < 0:
            raise ValueError("x must be >= 0")
        self.__x = a

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, a):
        """ y setter"""
        if type(a) is not int:
            raise TypeError("y must be an integer")
        elif a < 0:
            raise ValueError("y must be >= 0")
        self.__y = a

    def area(self):
        """ function that returns area of rectangle instance """
        return self.width * self.height

    def display(self):
        """ prints in stdout the Rectangle instance with the character # """
        for a in range(self.y):
            print('')
        for i in range(self.height):
            for k in range(self.x):
                print(' ', end='')
            for j in range(self.width):
                print("#", end='')
            print("")

    def __str__(self):
        """ overriding the default __str__ method """
        pt1 = "[Rectangle] ({}) {}/{} ".format(self.id, self.x, self.y)
        pt2 = "- {}/{}".format(self.width, self.height)
        return pt1 + pt2

    def update(self, *args, **kwargs):
        """ updates instance attributes """
        if len(args) > 0 and args is not None:
            i = 0
            while i < len(args):
                if i == 0:
                    self.id = args[0]
                elif i == 1:
                    self.width = args[1]
                elif i == 2:
                    self.height = args[2]
                elif i == 3:
                    self.x = args[3]
                else:
                    self.y = args[4]
                i += 1
            else:
                for key, value in kwargs:
                    if key == "id":
                        self.id = value
                    elif key == "width":
                        self.width = value
                    elif key == "height":
                        self.height = value
                    elif key == "x":
                        self.x = value
                    elif key == "y":
                        self.y = value
