#!/usr/bin/python3

""" writes an Object to a text file, using a JSON representation:
"""

import json


def save_to_json_file(my_obj, filename):

    """ Writes json to a file

    Returns:
        int: The number of char added
    """

    with open(filename, 'w', encoding='UTF-8') as file:
        num_char = json.dump(my_obj, file)
    return num_char
