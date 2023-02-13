#!/usr/bin/python3
"""
module contains function load_from_json_file
"""
import json


def load_from_json_file(filename):
    """function that creates an object from a json file"""
    with open(filename, mode="r") as f:
        data = json.loads(f.read())
    return data
