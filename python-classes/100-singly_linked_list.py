#!/usr/bin/python3
i"""Singly linked list"""


class Node:
    """List must be printed single"""

    def __init__(self,data):
        self.data = data

    @property
    """getter the attribute"""

    def data(self):
        return self._data

    @data.setter
    """setter the attribute"""

    def data(self,value):
        if type(value)!= int:
            raise TypeError("data must be an integer")

    def __init__(self,next_node):
        self.next_node = next_node

    @property
    """getter the attribute"""

    def next_node(self):
        return self.__next_node

    @next_node.setter
    """setter the attribute"""

    def next_node(self,value):
        if next_node!= None:
            raise TypeError("next_node must be a Node object")

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node  = None

