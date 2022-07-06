#!/usr/bin/python3
"""Converts json to string format
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
