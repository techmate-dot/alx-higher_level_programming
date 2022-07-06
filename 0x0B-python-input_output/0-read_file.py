#!/usr/bin/python3

""" print content of a file to the standard output"""


def read_file(filename=""):
    """
        args:
            filename - Name of the text file
        Returns: prints the content of the file to stdout
    """
    with open(filename, 'r', encoding='UTF8') as f:
        value = f.read()
        print(value)
