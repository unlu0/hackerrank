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

def print_singly_linked_list(node):
    while node:
        print(str(node.data))
        node = node.next

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
""" def setNext(head1,head2):
    hold = head1.next
    head1.next = head2
    next = head2.next
    head2.next = hold
    return hold,next """
""" def setLast(last, head):
    while head:
        last.next = head
        head = head.next
        last = last.next  """
""" def mergeLists(head1, head2):
    head = head1 if head1.data <= head2.data else head2
    prev = None
    while head1 and head2:
        if head1.data <= head2.data:
            prev = head1
            head1, head2 = setNext(head1,head2)
        else:
            prev = head1
            head2, head1 = setNext(head2,head1)

    if head1 is None:
        setLast(prev, head2)
    elif head2 is None:
        setLast(prev, head1)
    
    return head """

def setLast(result, head):
    while head:
        result.insert_node(head.data)
        head = head.next

def mergeListsNew(head1, head2):
    head = head1 if head1.data <= head2.data else head2
    result = head
    end = False
    while head1 or head2:
        while end or head1.data <= head2.data:
            head.next = head1.next
            head1 = head1.next
            if not head1:
                head.next = head2
                head = head.next
                end = True
                break
            head = head.next
        while end or head2.data <= head1.data:
            head.next = head2.next
            head2 = head2.next
            if not head2:
                head.next = head1
                head = head.next
                end = True
                break
            head = head.next
    
    return result

def mergeLists(head1, head2):
    result = SinglyLinkedList()
    prev = None
    while head1 and head2:
        if head1.data <= head2.data:
            result.insert_node(head1.data)
            prev = head1
            head1 = head1.next
        else:
            result.insert_node(head2.data)
            prev = head2
            head2 = head2.next

    if head1 is None:
        setLast(result, head2)
    elif head2 is None:
        setLast(result, head1)
    
    return result.head

if __name__ == '__main__':

    llist1 = SinglyLinkedList()
    llist1.insert_node(4)
    llist1.insert_node(5)
    llist1.insert_node(6)
    llist2 = SinglyLinkedList()
    llist2.insert_node(1)
    llist2.insert_node(2)
    llist2.insert_node(10)

    llist3 = mergeListsNew(llist1.head, llist2.head)

    print_singly_linked_list(llist3)

