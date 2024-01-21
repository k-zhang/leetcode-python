from unittest import TestCase

from implement_strstr import strstr


class Test(TestCase):
    def test_strstr(self):
        self.assertEqual(2, strstr("hello", "ll")),
        self.assertEqual(-1, strstr("aaaaa", "bba")),
        self.assertEqual(1, strstr("cabcabcd", "abc")),
        self.assertEqual(0, strstr("abcabcd", "abc")),
        self.assertEqual(-1, strstr("aaa", "aaaa")),
        self.assertEqual(0, strstr("aaa", "aaa")),
        self.assertEqual(4, strstr("mississippi", "issip")),
        self.assertEqual(-1, strstr("mississippi", "issipi")),
        self.assertEqual(11, strstr("aabcdeafghiajtjtjklmf", "ajtj")),
        self.assertEqual(0, strstr("", ""))
