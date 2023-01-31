#!/usr/bin/python3
"""LockedClass"""


class LockedClass:
    """prevents creating of an instance outside specified names"""
    __slots__ = ['first_name']
