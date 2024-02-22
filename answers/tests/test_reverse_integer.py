from unittest import TestCase

from reverse_integer import reverse_integer


class Test(TestCase):
    def test_reverse_integer(self):
        self.assertEqual(1, reverse_integer(1))
        self.assertEqual(0, reverse_integer(0))
        self.assertEqual(12, reverse_integer(21))
        self.assertEqual(123, reverse_integer(321))
        self.assertEqual(7463847412, reverse_integer(2147483647))
