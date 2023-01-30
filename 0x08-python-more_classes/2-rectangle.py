#!/usr/bin/python3
"""script that defines a Rectangle class"""


class Rectangle:
    """Class Rectangle that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """initialising an instance of the object"""
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
                raise TypeError("height must be >= 0")

    @property
    def width(self):
        """Retrieves width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width to value"""
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
        """Retrieves height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height to value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        else:
            if value >= 0:
                self.__height = value
                return self.__height
            else:
                raise TypeError("height must be >= 0")

    def area(self):
        """Area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)
