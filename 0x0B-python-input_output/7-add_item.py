#!/usr/bin/python3
"""Script that adds all arguments to a Python list, and saves them"""
import os
import sys
import json


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'
args = len(sys.argv)

if not os.path.isfile(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('[]')

if args > 1:
    data = load_from_json_file(filename)
    for i in range(1, args):
        data.append(sys.argv[i])
    save_to_json_file(data, filename)
