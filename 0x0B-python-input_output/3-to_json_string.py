#!/usr/bin/python3
"""
Function that returns the JSON representation
of an object(string)
"""
import json


def to_json_string(my_obj):
    """
    ``my_obj`` being the objcet to be serialized.
    Returns the JSON representation of ``my_obj``
    """
    return json.dumps(my_obj)
