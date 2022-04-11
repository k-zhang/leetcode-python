import unittest
from unittest import TestCase
from coin_change import *


class TestSolution(TestCase):
    def test_coin_change(self):
        solution = Solution()
        self.assertEqual(3, solution.coin_change([1, 2, 5], 11))
        self.assertEqual(3, solution.coin_change([1, 5, 8], 11))
        self.assertEqual(20, solution.coin_change([186,419,83,408], 6249))
        self.assertEqual(-1, solution.coin_change([2], 3))
        self.assertEqual(-1, solution.coin_change([3], 2))
        self.assertEqual(0, solution.coin_change([1], 0))
        self.assertEqual(1, solution.coin_change([1], 1))
        self.assertEqual(2, solution.coin_change([1], 2))


if __name__ == '__main__':
    unittest.main()