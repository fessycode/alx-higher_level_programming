#!/usr/bin/python3
"""Class of Square that define a square"""


class Square:
    """Declearing the class"""

    def __init__(self, size=0):
        """Initializing object/instance"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returning  square area of the object"""
        return (self.__size ** 2)

    @property
    def size(self):
        """A getter for instance attribute size
        Returns the value of ``__size``"""
        return self.__size

    @size.setter
    def size(self, size):
        """A setter for instance attribute size
        Sets a value for ``__size``"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
