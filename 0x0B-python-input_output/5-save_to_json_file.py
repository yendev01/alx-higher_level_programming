#!/usr/bin/python3
"""
module that contains a function, save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an object to a text file using JSON"""
    my_data = json.dumps(my_obj)
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(my_data)
