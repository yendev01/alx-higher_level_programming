#!/usr/bin/python3


def uppercase(str):
    for i in str:
        print("{:s}".format(chr(ord(i) - 32) if 97 <= ord(i) < 123 else i),
              end="")
    print("")
