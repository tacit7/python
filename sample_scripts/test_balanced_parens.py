import unittest
import balanced_parens

class TestBalancedParens(unittest.TestCase):
    def test_check_parens(self):
        self.assertTrue(balanced_parens.check_parens("()"))

    def test_unblananced_parens_right(self):
        self.assertFalse(balanced_parens.check_parens("())"))

    def test_unblananced__parens_left(self):
        self.assertFalse(balanced_parens.check_parens("(()"))
