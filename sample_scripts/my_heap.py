import math
from IPython import embed

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
        return math.floor((child_index - 1) / 2)

    def has_left_child(self, index):
        return self.left_child_index(index) < len(self.heap) - 1

    def has_right_child(self, index):
        return self.right_child_index(index) < len(self.heap) - 1

    def has_parent(self, index):
        return self.parent_index(index) >= 0

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

    def pop(self):
        element = self.heap[0]
        self.heap[0] = self.heap.pop
        self.heapifyDown()
        return element

    def add(self, element):
        self.heap.append(element)
        self.heapifyUp()

    def heapify_up(self):
        index = len(self.heap) - 1
        while self.has_parent(index) and self.needs_to_become_parent(index):
            self.swap(self.parent_index(index), index)
            index = self.parent_index(index)

        return self.heap

    def heapify_down(self):
        index = 0
        while(self.has_left_child(index)): # you only need to check the left child since there is no right without the left
            small_child_index = self.get_smallest_child_index(index)
            if self.heap[index] < self.heap[small_child_index]:
                break
            else:
                self.swap(index, small_child_index)
                index = small_child_index


        return self.heap


    def needs_to_become_parent(self, index):
        return self.parent(index) > self.heap[index]

    def get_smallest_child_index(self, index):
        child_index = self.left_child_index(index)

        if self.has_right_child(index) and self.right_child(index) < self.left_child(child_index):
            child_index = self.right_child_index(index)

        return child_index
