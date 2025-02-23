import unittest
from length_of_last_word import *

class TestLengthOfLastWord(unittest.TestCase):
    def test(self):
        self.assertEqual(length_of_last_word('hello world'), 5)
        self.assertEqual(length_of_last_word('helloworld'), 10)
        self.assertEqual(length_of_last_word('hello world my son'), 3)
        self.assertEqual(length_of_last_word('hello world my son    '), 3)


if __name__ == '__main__':
    unittest.main()

