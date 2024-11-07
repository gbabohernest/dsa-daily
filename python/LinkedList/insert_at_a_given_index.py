#!/usr/bin/python3

"""
Given the head of a LL, an index, and a value. Write a function that insert a given
node in the  LL at a given index and return the head of the List.
"""

from typing import Any


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

    @staticmethod
    def insert_at_given_index_recursively(head: 'Node', value: int, index: int) -> 'Node' or None:
        """
        Recursively insert a new node at a given index in the single LL
        :param head: current head of the LL
        :param value: value to insert
        :param index: index at which to insert the value
        :return: updated head of the LL

        """

        if head is None:
            print('Index out of bound, cannot insert')
            exit()

        if head is None and index == 0:
            # insert at the beginning of the list
            new_node = Node(value)
            new_node.next = head
            head = new_node
            return head

        if index == 0:
            new_node = Node(value)
            new_node.next = head
            return new_node

        head.next = Node.insert_at_given_index_recursively(head.next, value, index - 1)
        return head

    @staticmethod
    def insert_at_given_index_iteratively(head: 'Node', value: int, index: int) -> 'Node':
        """
        Inserts a node in a given LL at a particular index.

        :param head: current head of the LL
        :param value: value to insert
        :param index: index at which to insert the value
        :return: updated head of the LL
        """

        if index == 0:
            # Insert at the beginning of the LL
            new_node = Node(value)
            new_node.next = head
            head = new_node
            return head

        prev_node = None
        counter = 0
        current_node = head

        while current_node is not None and counter < index:
            # Traverse the LL to find the insertion point or Not
            prev_node = current_node
            current_node = current_node.next
            counter += 1

        if counter == index:
            # Insertion point is found
            new_node = Node(value)
            prev_node.next = new_node
            new_node.next = current_node

        else:
            # index is out of bound
            print('Index is out of bound, cannot insert a new node')
            exit()

        return head

    @staticmethod
    def print_linkedlist(head_node: 'Node') -> None:

        current_node = head_node
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


# create nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
f = Node(6)
# a -> b -> c -> d -> f
a.next = b
b.next = c
c.next = d
d.next = f

# Test
Node.print_linkedlist(Node.insert_at_given_index_iteratively(a, 5, 4))  # 1 -> 2 -> 3 -> 4 -> 5 -> 6
print()
Node.print_linkedlist(Node.insert_at_given_index_iteratively(a, 0, 0))  # 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
print()
Node.print_linkedlist(Node.insert_at_given_index_recursively(a, 55, 3))  # 1 -> 2 -> 3 -> 55 -> 4 -> 5 -> 6