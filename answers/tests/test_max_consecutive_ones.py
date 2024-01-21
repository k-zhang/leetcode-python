from unittest import TestCase

from max_consecutive_ones import find_max_consecutive_ones


class Test(TestCase):
    def test_find_max_consecutive_ones(self):
        self.assertEqual(4, find_max_consecutive_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]))
        self.assertEqual(4, find_max_consecutive_ones([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]))
        self.assertEqual(1, find_max_consecutive_ones([1]))
        self.assertEqual(0, find_max_consecutive_ones([0]))
        self.assertEqual(1, find_max_consecutive_ones([1, 0, 0, 1]))
        self.assertEqual(4, find_max_consecutive_ones([1, 1, 1, 1]))
        self.assertEqual(0, find_max_consecutive_ones([0, 0, 0, 0]))
