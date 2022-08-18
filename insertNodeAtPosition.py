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

def insertNodeAtPosition(llist, data, position):
    head = llist
    for i in range(position-1):
        head = head.next
    hold = head.next
    head.next = SinglyLinkedListNode(data)
    head.next.next = hold
    return llist


    # Write your code here

if __name__ == '__main__':

    llist = SinglyLinkedList()

    llist.insert_node(3)
    llist.insert_node(16)
    llist.insert_node(13)
    llist.insert_node(7)
    llist.insert_node(1)
    llist.insert_node(2)

    data = 5

    position = 3

    llist_head = insertNodeAtPosition(llist.head, data, position)
