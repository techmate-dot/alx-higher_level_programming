#!/usr/bin/python3

""" A function that append text to a file """


def append_write(filename="", text=""):

    """
        args:
            filename (str)- Name of the txt file
            text (str) - text to write
        Returns: the number of characters added
    """
    with open(filename, 'a', encoding='UTF8') as f:
        num_of_char = f.write(text)
    return num_of_char
