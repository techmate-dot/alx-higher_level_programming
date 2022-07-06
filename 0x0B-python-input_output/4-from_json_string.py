#!/usr/bin/python3

""" From json string to json
    """

import json


def from_json_string(my_str):
    """returns an object (Python data structure) represented by a JSON string

    Args:
        my_str (str): file to convert

    Returns:
        obj: An object (Python data structure) represented by a JSON string
    """
    conv_json = json.loads(my_str)
    return conv_json
