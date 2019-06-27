from p9 import Solution
import unittest

class TestP9(unittest.TestCase):

    def test_palindrome(self):

        a = Solution(13340).isPalindrome()
        self.assertEqual(a, False)

        a = Solution(-1).isPalindrome()
        self.assertEqual(a, False)

        a = Solution(11).isPalindrome()
        self.assertEqual(a, True)

        a = Solution(143341).isPalindrome()
        self.assertEqual(a, True)

        a = Solution(10).isPalindrome()
        self.assertEqual(a, False)

        a = Solution(1000000001).isPalindrome()
        self.assertEqual(a, True)
