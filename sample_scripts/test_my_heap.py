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

    def test_needs_to_become_parent(self):
        heap = [
                 0,
            1,        2,
           11,12,  21, 22]
        h = my_heap.MyHeap(heap)

        self.assertFalse(h.needs_to_become_parent(6))
        self.assertFalse(h.needs_to_become_parent(2))

        heap = [
                 0,
            1,        2,
            11,12,  21, 0]
        h = my_heap.MyHeap(heap)

        self.assertTrue(h.needs_to_become_parent(6))

    def test_heapify_down(self):
        heap = [
                 0,
            1,        2,
            11,12,  21, 22]
        h = my_heap.MyHeap(heap)

        self.assertTrue(h.heapify_down())

    def test_heapify_up(self):
        heap = [
                 0,
            1,        22,
            11,12,  21, 2]
        h = my_heap.MyHeap(heap)

        self.assertTrue(h.heapify_up())

