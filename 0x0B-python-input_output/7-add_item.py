#!/usr/bin/python3
"""
module that ...
"""
from os.path import exists
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = \
  __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
if exists(filename):
    my_obj = load_from_json_file(filename)
else:
    my_obj = []
my_obj.extend(sys.argv[1:])
save_to_json_file(my_obj, filename)
