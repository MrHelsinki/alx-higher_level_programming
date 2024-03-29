#!/usr/bin/python3
""" define sqr class"""


class Square:
    """Square me good sir
    Attributes:
        __size (int): size probably
    """

    def __init__(self, size=0):
        """ def size
        Args:
            size (int): size probably
        """
        self.size = size

    @property
    def size(self):
        """getter for __size"""

        return self.__size

    @size.setter
    def size(self, value):
        """setter for __size
        Args:
            value (int): value to set
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ return area of Sqr"""
        return self.size**2
