#!/usr/bin/python3
uppercase = __import__('8-uppercase').uppercase

uppercase("holberton")
def uppercase(str):
    """Print a string in uppercase."""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            i = chr(ord(c) - 32)
    print("{}".format(i), end="")
    print("")
