import unittest
from p121 import maxProfitV1
from p121 import maxProfitV2

class TestP121(unittest.TestCase):
    def test_base(self):
        stocks = [7,1,5,3,6,4]
        a = maxProfitV1(stocks)
        self.assertEqual(a, 5)

        stocks = [7,1,100,3,6,4]
        a = maxProfitV1(stocks)
        self.assertEqual(a, 3)

    def test_v2(self):
        stocks = [7,1,5,3,6,4]
        a = maxProfitV2(stocks)
        self.assertEqual(a, 5)

        stocks = [7,1,100,3,6,4]
        a = maxProfitV2(stocks)
        self.assertEqual(a, 99)
