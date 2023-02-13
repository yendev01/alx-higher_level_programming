#!/usr/bin/python3
"""
module that contains a function to_json_string
"""
import json


def to_json_string(my_obj):
    """function that returns JSON representation of an object
    Args:
       my_obj

    Raises:
        Exception when the object can't be encoded
    """
    return json.dumps(my_obj)
