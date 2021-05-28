import unittest
from longest_substring_without_repeating_characters import *


class MyTestCase(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(0, solution.length_of_longest_substring(""))
        self.assertEqual(1, solution.length_of_longest_substring("a"))
        self.assertEqual(3, solution.length_of_longest_substring("abcabcbb"))
        self.assertEqual(1, solution.length_of_longest_substring("bbbbb"))
        self.assertEqual(3, solution.length_of_longest_substring("pwwkew"))
        self.assertEqual(2, solution.length_of_longest_substring("abbbbbba"))


if __name__ == '__main__':
    unittest.main()
