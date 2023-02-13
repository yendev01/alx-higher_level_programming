#!/usr/bin/python3
"""
module which contains a function, write_file
"""


def write_file(filename="", text=""):
    """funtion that writes text into a file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        write_data = f.write(text)
    return write_data
