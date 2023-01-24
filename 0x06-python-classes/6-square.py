#!/usr/bin/python3


class Square:
    """Class that defines a square as well as its area computation"""
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        if type(position) is not tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            if position[0] < 0 or position[1] < 0:
                raise \
                 TypeError("position must be a tuple of 2 positive integers")
            else:
                self.__position = position

    def area(self):
        """Returns the current square area"""
        return self.__size * self.__size

    @property
    def size(self):
        """To retrieve"""
        return self.__size

    @size.setter
    def size(self, value):
        """ To set it"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        """ printing a square"""
        if (self.__size == 0):
            print()
        else:
            for l in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    @property
    def position(self):
        """to retrieve it """
        return self.__position

    @position.setter
    def position(self, value):
        """to set it"""
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            if value[0] < 0 or value[1] < 0:
                raise \
                 TypeError("position must be a tuple of 2 positive integers")
            else:
                self.__position = value
