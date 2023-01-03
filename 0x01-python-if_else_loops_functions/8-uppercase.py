#!/usr/bin/python3


def uppercase(str):
    for i in str:
        print("{:s}".format(chr(ord(i) - 32)))
