import unittest
from median_of_two_sorted_arrays import *


class MyTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(2.0, find_median_sorted_arrays([1, 3], [2]))
        self.assertEqual(2.0, find_median_sorted_arrays([1, 2, 3], []))
        self.assertEqual(2.5, find_median_sorted_arrays([1, 2, 3, 4], []))
        self.assertEqual(2.5, find_median_sorted_arrays([], [1, 2, 3, 4]))
        self.assertEqual(2.5, find_median_sorted_arrays([1, 2], [3, 4]))
        self.assertEqual(0.0, find_median_sorted_arrays([0, 0], [0, 0]))
        self.assertEqual(1.0, find_median_sorted_arrays([], [1]))
        self.assertEqual(2.0, find_median_sorted_arrays([2], []))
        self.assertEqual(0.0, find_median_sorted_arrays([], []))


if __name__ == '__main__':
    unittest.main()
