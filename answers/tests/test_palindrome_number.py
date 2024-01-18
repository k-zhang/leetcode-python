from unittest import TestCase

from palindrome_number import is_palindrome


class Test(TestCase):
    def test_is_palindrome(self):
        self.assertEqual(True, is_palindrome(0))
        self.assertEqual(True, is_palindrome(5))
        self.assertEqual(True, is_palindrome(121))
        self.assertEqual(False, is_palindrome(-121))
        self.assertEqual(False, is_palindrome(10))
        self.assertEqual(False, is_palindrome(2147483647))
        self.assertEqual(False, is_palindrome(-2147483648))
