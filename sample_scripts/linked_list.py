from node import Node
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            self.head.next = Node(data)
