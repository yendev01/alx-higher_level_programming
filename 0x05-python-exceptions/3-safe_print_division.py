#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        c = (a / b) * 1.0
    except Exception:
        c = "None"
    finally:
        print("Inside result: {}".format(c))
    return c
