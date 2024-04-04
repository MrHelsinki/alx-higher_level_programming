#!/usr/bin/python3
"""
Defines an empty class Rectangle
"""


class Rectangle:
	""" define Rectangle"""
	def __init__(self, width=0 , height=0):
		""" set necessary attributes"""
		self.width = width
		self.height = height
	
	@property
	def width(self):
		""" width getter """
		return self.__width
	
	@width.setter
	def width(self, value):
		""" width setter """
		if type(value) != int:
			raise TypeError("width must be an integer")
		elif value < 0:
			raise ValueError("width must be >= 0")
		else:
			self.__width = value
	
	@property
	def height(self):
		""" height getter """
		return self.__height
	
	@height.setter
	def height(self, value):
		""" height setter """
		if type(value) != int:
			raise TypeError("height must be an integer")
		elif value < 0:
			raise ValueError("height must be >= 0")
		else:
			self.__height = value

