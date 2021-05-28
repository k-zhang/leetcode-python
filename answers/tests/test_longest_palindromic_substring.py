import unittest
from longest_palindromic_substring import *


class MyTestCase(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual("bb", solution.longest_palindrome("cbbd"))
        self.assertEqual("a", solution.longest_palindrome("ac"))
        self.assertEqual("e", solution.longest_palindrome("eabcd"))
        self.assertEqual("aca", solution.longest_palindrome("aacabdkacaa"))


if __name__ == '__main__':
    unittest.main()
