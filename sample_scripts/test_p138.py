import unittest
import p138
from node import RanNode

class TestP138(unittest.TestCase):

    def test_it_copies(self):
        a = RanNode(1)
        b = RanNode(2)
        c = RanNode(3)
        d = RanNode(4)
        a.next = b
        b.next = c
        c.next = d
        b.random = a
        a.random = b
        c.random = d
        d.random = d



        copy = p138.copy_random_list(a)

        self.assertEqual(copy.value, a.value)
        self.assertEqual(copy.next.value, a.next.value)
        self.assertEqual(copy.next.value, a.next.value)
        self.assertNotEqual(copy, a)



