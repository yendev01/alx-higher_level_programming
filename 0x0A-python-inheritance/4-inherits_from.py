#!/usr/bin/python3
"""
module that contains the inherits_from function 
"""


def inherits_from(obj, a_class):
    """returns true if obj is a subclass of a_class..."""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
