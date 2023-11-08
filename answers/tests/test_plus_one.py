import unittest
from unittest import TestCase
from plus_one import *


class MyTestCase(TestCase):
    def test_plus_one(self):
        self.assertEqual([1], plus_one([0]))
        self.assertEqual([1, 2, 4], plus_one([1, 2, 3]))
        self.assertEqual([4, 3, 2, 2], plus_one([4, 3, 2, 1]))
        self.assertEqual([4, 3, 3, 0], plus_one([4, 3, 2, 9]))
        self.assertEqual([4, 4, 0, 0], plus_one([4, 3, 9, 9]))
        self.assertEqual([5, 0, 0, 0], plus_one([4, 9, 9, 9]))
        self.assertEqual([1, 0, 0, 0, 0], plus_one([9, 9, 9, 9]))


if __name__ == '__main__':
    unittest.main()
