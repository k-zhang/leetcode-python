import unittest
from longest_substring_without_repeating_characters import *


class MyTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(0, length_of_longest_substring(""))
        self.assertEqual(1, length_of_longest_substring("a"))
        self.assertEqual(3, length_of_longest_substring("abcabcbb"))
        self.assertEqual(1, length_of_longest_substring("bbbbb"))
        self.assertEqual(3, length_of_longest_substring("pwwkew"))
        self.assertEqual(2, length_of_longest_substring("abbbbbba"))


if __name__ == '__main__':
    unittest.main()
