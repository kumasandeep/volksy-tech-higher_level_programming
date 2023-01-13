#!/usr/bin/python3
"""This module contains a class MyList that inherits from list.
"""


class MyList(list):
    """Class MyList that inherits from list.
    Arguments:
        list (list) -- list object.
    """

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort).
        """
        print(sorted(self))
