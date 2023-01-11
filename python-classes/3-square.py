#!/usr/bin/python3
"""Area of Square"""


class Square:
    """Square size"""
    def __init__(self, size=0):
         """Constructor"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size

    def area(self):
        """Area of Square"""
        return(self.__size * self.__size)
