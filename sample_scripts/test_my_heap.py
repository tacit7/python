import unittest
import my_heap

class TestMyHeap(unittest.TestCase):

    def test_left_child(self):
        heap = [
                 0,
            1,        2,
           11,12,  21, 22]
        h = my_heap.MyHeap(heap)

        self.assertEqual(h.left_child(1), 11)
        self.assertEqual(h.left_child(2), 21)

    def test_right_child(self):
        heap = [
                 0,
            1,        2,
           11,12,  21, 22]
        h = my_heap.MyHeap(heap)

        self.assertEqual(h.right_child(1), 12)
        self.assertEqual(h.right_child(2), 22)

    def test_parent(self):
        heap = [
                 0,
            1,        2,
           11,12,  21, 22]
        h = my_heap.MyHeap(heap)

        self.assertEqual(h.parent(1), 0)
        self.assertEqual(h.parent(2), 0)
