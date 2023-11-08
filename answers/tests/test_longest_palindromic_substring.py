import unittest
from longest_palindromic_substring import *


class MyTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual("bb", longest_palindrome("cbbd"))
        self.assertEqual("a", longest_palindrome("ac"))
        self.assertEqual("e", longest_palindrome("eabcd"))
        self.assertEqual("aca", longest_palindrome("aacabdkacaa"))


if __name__ == '__main__':
    unittest.main()
