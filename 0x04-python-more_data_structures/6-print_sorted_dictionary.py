#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    key_list = sorted(list(map(lambda x	:	x,
                      a_dictionary.keys())))
    for i in key_list:
        print("{}: {}".format(i, a_dictionary.get(i)))
