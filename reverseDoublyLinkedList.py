#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'reverse' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts INTEGER_DOUBLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def changePrevAndNext(node):
    hold = node.next
    node.next = node.prev
    node.prev = hold

def reverse(llist):
    # Write your code here
    head = llist
    while head is not None:
        changePrevAndNext(head)
        prev = head
        head = head.prev 

    return prev

if __name__ == '__main__':

    llist = DoublyLinkedList()

    llist.insert_node(1)
    llist.insert_node(2)
    llist.insert_node(3)
    llist.insert_node(4)
    llist.insert_node(5)
    llist.insert_node(6)
    llist.insert_node(7)

    llist1 = reverse(llist.head)

    print_doubly_linked_list(llist1)