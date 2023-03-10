#!/usr/bin/python3
"""script that defines a Rectangle class"""


class Rectangle:
    """Class Rectangle that defines a rectangle"""
    print_symbol = "#"
    number_of_instances = 0

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
        Rectangle.number_of_instances += 1

    def __str__(self):
        """prints the rectangle with character #"""
        st = ""
        if self.__height == 0 or self.__width == 0:
            return st
        for i in range(self.__height):
            for j in range(self.__width):
                st += str(self.print_symbol)
            st += "\n"
        return st[:-1]

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
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __repr__(self):
        """return a string representation of the rectangle..."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """detects instance deletion"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() == rect_2.area():
                return rect_1
            else:
                if rect_1.area() > rect_2.area():
                    return rect_1
                else:
                    return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
