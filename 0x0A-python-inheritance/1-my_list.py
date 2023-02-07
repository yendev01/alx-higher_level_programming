#!/usr/bin/python3
"""
contains a class that inherits another class
"""


class MyList(list):
    """inherits from list"""
    def __init__(self):
        """ initialises the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
