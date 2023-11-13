import unittest
from unittest import TestCase
from is_subsequence import is_subsequence


class Test(TestCase):
    def test_is_subsequence(self):
        self.assertEqual(True, is_subsequence("abc", "ahbgdc"))
        self.assertEqual(False, is_subsequence("axc", "ahbgdc"))
        self.assertEqual(True, is_subsequence("", ""))
        self.assertEqual(True, is_subsequence("", "a"))


if __name__ == '__main__':
    unittest.main()