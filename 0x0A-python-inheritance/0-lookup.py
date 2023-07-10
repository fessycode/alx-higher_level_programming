#!/usr/bin/python3
def lookup(obj):
    """ The function that returns the list of available attributes
        and methods of an object

    Args:
        obj: instance of the class

    Returns:
        List of attributes
    """

    return dir(obj)
