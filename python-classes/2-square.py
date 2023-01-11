#!/usr/bin/python3
"""Validation of size"""


class Square:
    """Validation of size"""
    def __init__(self, size=0):
        """Constructer"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
