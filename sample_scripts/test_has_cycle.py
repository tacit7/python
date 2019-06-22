import unittest
import has_cycle
import node

class TestHasCycle(unittest.TestCase):
    def test_circle_linked_list(self):

        a = node.node('a')
        b = node.node('b')
        c = node.node('c')
        d = node.node('d')
        e = node.node('e')

        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = c

        self.assertTrue(has_cycle.has_cycle(a))
