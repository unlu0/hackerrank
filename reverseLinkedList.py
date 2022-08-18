#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'reverse' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def reverse(head):
    # Write your code here
    holder = []
    holder.insert(0,head.data)
    while head.next is not None:
        head = head.next
        holder.insert(0,head.data)
    llist = SinglyLinkedList()
    for i in holder:
        llist.insert_node(i)

    return llist.head

    

if __name__ == '__main__':
    llist = SinglyLinkedList()

    llist.insert_node(1)
    llist.insert_node(2)
    llist.insert_node(3)
    llist.insert_node(4)
    llist.insert_node(5)

    llist1 = reverse(llist.head)

