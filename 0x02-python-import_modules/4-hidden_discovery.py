#!/usr/bin/python3

import hidden_4

if __name__ == '__main__':
    files = dir(hidden_4)
    length = len(files)

    for i in range(length):
        if files[i][:2] != '__':
            print(files[1])
