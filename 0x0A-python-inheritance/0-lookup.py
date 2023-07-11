#!/usr/bin/python3
"""
Simple programme that returns a list of available
attributes and methods available in an object.
"""


def lookup(obj):
    """
    Returns a list of objects attributes and methods
    """
    return dir(obj)
