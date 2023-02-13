#!/usr/bin/python3
"""
module which contains a function, read_file
"""


def read_file(filename=""):
    """funtion that reads a text file(UTF8) and prints to stdout"""
    with open(filename, encoding="utf-8") as f:
        read_text = f.read()
    print("{:s}".format(read_text), end="")
