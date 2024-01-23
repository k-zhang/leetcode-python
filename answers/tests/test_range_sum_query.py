from unittest import TestCase

from range_sum_query import RangeSumQuery


class TestRangeSumQuery(TestCase):
    def test(self):
        num_array = RangeSumQuery([-2, 0, 3, -5, 2, -1])

        self.assertEqual(1, num_array.sum_range(0, 2))
        self.assertEqual(-1, num_array.sum_range(2, 5))
        self.assertEqual(-3, num_array.sum_range(0, 5))
