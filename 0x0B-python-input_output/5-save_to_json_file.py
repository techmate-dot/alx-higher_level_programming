#!/usr/bin/python3

""" writes an Object to a text file, using a JSON representation:
"""

import json


def to_json_string(my_obj):
    """  A function that returns the JSON representation of an object (string):

    Args:
        my_obj (str): The string to be converted

    Returns:
        str: returns the JSON representation of an object (string):
    """

    formated_str = json.dumps(my_obj)
    return formated_str


def save_to_json_file(my_obj, filename):

    """ Writes json to a file

    Returns:
        int: The number of char added
    """

    formated_str = to_json_string(my_obj)

    with open(filename, 'w', encoding='UTF-8') as file:
        num_char = file.write(formated_str)
    return num_char
