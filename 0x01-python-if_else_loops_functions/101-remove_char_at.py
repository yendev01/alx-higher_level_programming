#!/usr/bin/python3


def remove_char_at(str, n):
    count = 0
    strCopy = ""
    for i in str:
        if count == n:
            count += 1
            continue
        else:
            strCopy += i
            count += 1
    return strCopy
