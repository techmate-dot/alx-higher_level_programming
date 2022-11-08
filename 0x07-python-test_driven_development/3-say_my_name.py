#!/bin/usr/python3

""" A function that says my name
    """


def say_my_name(first_name, last_name=""):
    """Returns the first and last name

    Args:
        first_name (str): the first name
        last_name (str, optional): last name. Defaults to "".

    Raises:
        TypeError: If first_name is not a str
        TypeError: If last_name is not a str

    Returns:
        string: The first and last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name,str):
        raise TypeError("last_name must be a string")
    else:
        print(f"{first_name} {last_name}")


if __name__ == '__main__':
    say_my_name()
    say_my_name("Walter", "White")
    say_my_name("Bob")
    try:
        say_my_name(12, "White")
    except Exception as e:
        print(e)
