#!/usr/bin/python3


def weight_average(my_list=[]):
    if not my_list:
        return 0
    denominator = 0
    numerator = 0
    for i in my_list:
        a, b = i
        denominator += b
        numerator += a*b
    return (numerator/denominator)
