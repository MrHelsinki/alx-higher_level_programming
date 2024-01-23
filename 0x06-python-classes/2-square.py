#!/usr/bin/python3

""" Square Square Square"""


class Square:
    """ Square class with init size
    Attributes:
        __size (int): size ... maybe ?
    """

    def __init__(self, size):
        """ init the square
        Args:
            size (int): size ... probably
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
