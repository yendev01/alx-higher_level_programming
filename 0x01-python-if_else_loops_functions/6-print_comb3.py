#!/usr/bin/python3
for i in range(8):
    for j in range(10):
        if j > i:
            print("{:d}{:d}".format(i, j), end=", ")
print("{:d}{:d}".format(i + 1, j))
