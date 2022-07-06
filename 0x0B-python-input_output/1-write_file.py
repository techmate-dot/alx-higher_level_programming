#!/usr/bin/python3

"""Write to a file"""


def write_file(filename="", text=""):
    """
        Args:
            filename - name of the file you want to write to
            ext - The the text you want to write
    """

    with open(filename, 'w', encoding='UTF8') as f:
        num_char = f.write(text)
    return num_char
