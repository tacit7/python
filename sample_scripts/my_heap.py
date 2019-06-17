import math

class MyHeap(object):
    def __init__(self, lst):
        self.heap = lst

    def heap(self):
        return self.heap

    def left_child_index(self, parent_index):
        return 2 * parent_index + 1

    def right_child_index(self, parent_index):
        return 2 * parent_index + 2

    def parent_index(self, child_index):
        return (child_index - 1) / 2

    def has_left_child(self, index):
        return self.left_child_index(index) < len(self.heap) - 1

    def has_right_child(self, index):
        return self.right_child_index(index) < len(self.heap) - 1

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def left_child(self, index):
        return self.heap[self.left_child_index(index)]

    def right_child(self, index):
        return self.heap[self.right_child_index(index)]

    def parent(self, index):
        return self.heap[math.floor(self.parent_index(index))]

    def swap(self, index1, index2):
        tmp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = tmp

    def poll(self):
        element = self.heap[0]
        self.heap[0] = self.heap.pop
        self.heapifyDown()
        return element

    def add(self, element):
        self.heap.append(element)
        self.heapifyUp()
