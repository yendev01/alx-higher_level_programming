#!/usr/bin/python3


class Rectangle:
    """
    class that defines a rectangle
    """

    def __init__(self, width=0, height=0):
        """ instantiating the rectangle"""
        self.__height = height
        if type(width) is not int:
            raise TypeError("width must be an integer")
        else:
            if width >= 0:
                self.__width = width
            else:
                raise ValueError("width must be >= 0")

        if type(height) is not int:
            raise TypeError("height must be an integer")
        else:
            if height >= 0:
                self.__height = height
            else:
                raise ValueError("height must be >= 0")

    @property
    def width(self):
        """to retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """to set width to value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        else:
            if value >= 0:
                self.__width = value
                return self.__width
            else:
                raise ValueError("width must be >= 0")

    @property
    def height(self):
        """to retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """to set height to value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        else:
            if value >= 0:
                self.__height = value
                return self.__height
            else:
                raise ValueError("height must be >= 0")
