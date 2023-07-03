#!/usr/bin/python3
""" This module contain the class of rectangle
"""


class Rectangle:
    """ The class that define rectangle"""
    def __init__(self, width=0, height=0):
        """ Instantiation with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Method of returning width
        """
        return self.__width

    @property
    def height(self):
        """Method of returning height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """ Width setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ Height setter
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
