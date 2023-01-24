#!/usr/bin/python3
"""class square definition"""


class Square:
    """Class that defines a square as well as its area computation"""
    def __init__(self, size=0):
        """initializes a square with size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """Returns the current square area"""
        return self.__size * self.__size
