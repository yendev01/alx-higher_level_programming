#!/usr/bin/python3
"""module that contains class BaseGeometry"""


class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        """method that raises an Exception with a message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method that validates value"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than value".format(name))
        
