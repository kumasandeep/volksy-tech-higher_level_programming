#!/usr/bin/python3
"""String"""


class Square:
    """String Size"""

    def __init__(self,size=0):
            self.size = size

    @property
    def size(self):
        return self_size

    @size.setter
    def size(self, value):
        if type(value)!= int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self._size*self._size


