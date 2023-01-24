#!/usr/bin/python3
"""class Definition"""


class Square:
    """class that defines a square"""
    def __init__(self, size=0):
        """initializes a square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
