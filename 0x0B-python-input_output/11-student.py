#!/usr/bin/python3
"""
Class that defines a student by
- first_name
- last_name
- age
"""


class Student:
    """
    All member of the class will be having a
    public method ``to_json()`` which will return
    a dictionary representation of the member of
    the class.
    """

    def __init__(self, first_name, last_name, age):
        """
        Instantiation of the class Student with the
        following attributes, expected to be defined:
        - first_name
        - last_name
        - age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the
        member of the class.
        """
        if attrs is None:
            return self.__dict__
        v_attrs = []
        for n in attrs:
            if n in self.__dict__.keys():
                v_attrs.append(n)
        return {x: self.__dict__[x] for x in v_attrs}

    def reload_from_json(self, json):
        """
        Rebuilds class member/instance attributes
        from ``json``, with ``json`` assumed to always
        be a dictionary.
        """
        for n in json:
            self.__dict__[n] = json[n]
