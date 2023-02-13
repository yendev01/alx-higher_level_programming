#!/usr/bin/python3
import json
"""
module that contains a function from_json_string
"""


def from_json_string(my_str):
    """function that returns an object represented by json"""
    data = json.loads(my_str)
    return data
