from unittest import TestCase

from armstrong_number import is_armstrong


class Test(TestCase):
    def test_is_armstrong(self):
        self.assertEqual(True, is_armstrong(153))
        self.assertEqual(False, is_armstrong(123))
        self.assertEqual(False, is_armstrong(9234567))
