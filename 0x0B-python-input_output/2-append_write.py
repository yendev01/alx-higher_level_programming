#!/usr/bin/python3
"""
module which contains a function, append_write
"""


def append_write(filename="", text=""):
    """funtion that appends a string at the end of a text file"""
    with open(filename, mode="a", encoding="utf-8") as f:
        append_data = f.write(text)
    return append_data
