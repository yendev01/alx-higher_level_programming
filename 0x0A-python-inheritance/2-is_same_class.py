#!/usr/bin/python3
"""
script that contains a function which returns true if the
object is exactly an instance of the specified class; otherwise false
"""


def is_same_class(obj, a_class):
    """..."""
    if type(obj) == a_class:
        return True
    return False
