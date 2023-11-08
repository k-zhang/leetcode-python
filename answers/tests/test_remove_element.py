from unittest import TestCase
from remove_element import remove_element


class Test(TestCase):
    def test_remove_element(self):
        self.assertEqual(0, remove_element([], 3))
        self.assertEqual(1, remove_element([1], 3))
        self.assertEqual(0, remove_element([3], 3))
        self.assertEqual(1, remove_element([1, 1, 2], 1))
        self.assertEqual(2, remove_element([1, 1, 2], 2))
        self.assertEqual(2, remove_element([1, 1, 2], 2))
        self.assertEqual(2, remove_element([3, 2, 2, 3], 3))
        self.assertEqual(5, remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2))
        self.assertEqual(11, remove_element([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 100))
