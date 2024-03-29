import unittest

from two_sum import two_sum


class Test(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual([0, 1], sorted(two_sum([2, 7, 1, 5], 9)))
        self.assertEqual([1, 2], sorted(two_sum([3, 2, 4], 6)))
        self.assertEqual([0, 1], sorted(two_sum([3, 3], 6)))
        self.assertEqual([0, 2], sorted(two_sum([3, 6, -1], 2)))
        self.assertEqual([2, 3], sorted(two_sum([1, 5, 0, 0], 0)))


if __name__ == '__main__':
    unittest.main()
