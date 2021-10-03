#!/usr/bin/python3
class Node():
    '''Describes a node
        Args:
        data (int): Integer representing the data for the node
        next_node (Node): Represents the next node in the list
    '''
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        '''
         Updates the value for the data
        '''
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList():
    '''
        Inserts a node into a liked list
    '''
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        '''
            Inserts the nodes in a sorted fashion in increasing order
            Args:
                Value (int): The value of the node
        '''
        node = Node(value)
        tmp = self.__head
        # Checks if the head is None to then add the first node.
        if self.__head is None:
            self.__head = node
            return
        # Checks if the first node is less than the new node.
        if node.data < tmp.data:
            node.next_node = tmp
            self.__head = node
            return
        # Iterates and checks if the next node is more or less than new node.
        while tmp.next_node is not None:
            if tmp.next_node.data < node.data:
                tmp = tmp.next_node
            else:
                node.next_node = tmp.next_node
                tmp.next_node = node
                return
        tmp.next_node = node

    def __str__(self):
        tmp = self.__head
        if tmp is None:
            return ("")
        while tmp.next_node is not None and tmp:
            print(tmp.data)
            tmp = tmp.next_node
        return (str(tmp.data))
