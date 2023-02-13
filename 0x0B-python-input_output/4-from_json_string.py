#!/usr/bin/python3
"""
module that contains a function from_json_string
"""
import json


def from_json_string(my_str):
    """function that returns an object represented by json"""
    data = json.loads(my_str)
    return data
