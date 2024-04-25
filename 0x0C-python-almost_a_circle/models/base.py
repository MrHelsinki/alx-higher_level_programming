#!/usr/bin/python3

""" Define Base Class"""


class Base:
    """Base Class

    Private Class Attributes:
        __nb_objects (int): Number of instances
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init func
        Args:
            id (int): id of new instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
