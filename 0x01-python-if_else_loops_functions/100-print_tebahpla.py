#!/usr/bin/python3

for i in range(26):
    print("{:s}".format(chr(122 - i) if (122 - i) % 2 == 0
          else chr(90 - i)), end="")
