#!/usr/bin/python3
"""
script that contains class BaseGeometry
"""

class BaseGeometry():
    """class with method area(self) and raises an exception"""
    def area(self):
        """raises 'area() is not implemented' exception"""
        raise Exception("area() is not implemented")
