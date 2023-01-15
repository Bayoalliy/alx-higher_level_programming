#!/usr/bin/python3
""" In this module, two classes are created
to define a node and a singly linked list respectively
"""


class Node:
    """ A class representing a Node in C"""
    node_count = 0
    tail = None

    def __init__(self, data, next_node=None):
        self._data = data
        self._next_node = next_node
        Node.node_count += 1

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None or isinstance(value, Node) is False:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """ A class defining a singlyLinkedList"""
    def __init__(self):
        self._head = None

    def __str__(self):
        lst = ""
        noda = self._head
        for i in range(Node.node_count):
            lst += str(noda._data)
            if i != Node.node_count - 1:
                lst += "\n"
            noda = noda._next_node
        return lst

    def sorted_insert(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        if Node.node_count == 0:
            self._head = Node(value)
            Node.tail = self._head
        else:
            new_node = Node(value)
            if new_node._data < self._head._data:
                new_node._next_node = self._head
                self._head = new_node
            else:
                ptr = self._head
                while ptr._next_node is not None:
                    if new_node.data < ptr.next_node._data:
                        new_node._next_node = ptr._next_node
                        ptr._next_node = new_node
                        break
                    ptr = ptr._next_node
                else:
                    Node.tail._next_node = new_node
                    Node.tail = new_node
