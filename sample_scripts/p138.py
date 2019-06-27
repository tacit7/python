from node import *


def copy_random_list(head):
    copied_list = RanNode(0)
    cached_random = {}
    traversing_node = head
    previous = True

    copied_head = copied_list
    while traversing_node is not None:
        copied_list.value = traversing_node.value
        copied_list.next  = RanNode(0)
        copied_list = copied_list.next

        traversing_node = traversing_node.next

    return copied_head

