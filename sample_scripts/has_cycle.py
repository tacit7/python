import node
import time

def has_cycle(node_head):
    if node_head == None:
        return false

    fast = node_head.next
    slow = node_head

    while fast != None and fast.next != None and slow != None:
        if fast == slow:
            return True

        fast = fast.next.next
        slow = slow.next

    return False
