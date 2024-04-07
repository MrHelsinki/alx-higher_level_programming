#!/usr/bin/python3

""" Define rectangle subclass"""
from models.base import Base


class Rectangle(Base):
    """ rectangle subclass"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ rectangle subclass
        Args:
            width (int): width
            height (int): height
            x (int): x coordinate
            y (int): y coordinate
            id (int): id of new rec
        Raises:
            TypeError: if width || height is not int
            ValueError: if width || height is lower or equal to 0
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError(" width value must be of type (int)")
        elif value <= 0:
            raise ValueError("width value must be higher than 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError(" height value must be of type (int)")
        elif value <= 0:
            raise ValueError("height value must be higher than 0")
        else:
            self.__height = value

    @property
    def x(self):
        """x coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError(" x value must be of type (int)")
        elif value < 0:
            raise ValueError("x value must be higher than 0")
        else:
            self.__x = value

    @property
    def y(self):
        """y coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError(" y value must be of type (int)")
        elif value < 0:
            raise ValueError("y value must be higher than 0")
        else:
            self.__y = value
