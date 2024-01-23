#!/usr/bin/python3

""" Square Square Square"""


class Square:
    """ Square class with init size
    Attributes:
        __size (int): size maybe ?
    """

    def __init__(self, size=0):
        """ init the square
        Args:
            size (int): size most probably
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ return area of said square"""

        return self.__size**2
