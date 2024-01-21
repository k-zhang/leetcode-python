from unittest import TestCase

from isomorphic_strings import is_isomorphic


class Test(TestCase):
    def test_is_isomorphic(self):
        self.assertEqual(True, is_isomorphic('egg', 'add'))
        self.assertEqual(False, is_isomorphic('foo', 'bar'))
        self.assertEqual(True, is_isomorphic('paper', 'title'))
        self.assertEqual(True, is_isomorphic('c', 'a'))
        self.assertEqual(False, is_isomorphic('badc', 'baba'))
