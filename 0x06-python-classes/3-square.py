#!/usr/bin/python3
"""Class Square that define a square"""


class Square:
    """Declearing class"""

    def __init__(self, size=0):
        """Initializing object/instance"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returning the square of an object"""
        return (self.__size ** 2)
