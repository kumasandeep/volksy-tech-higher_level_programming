#!/usr/bin/python3
"""creating class """


class Square:
    """class for square"""

    def __init__(self, size=0):
        """constructor"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size

    def area(self):
        """area for square"""
        return  (self._size * self._size)
