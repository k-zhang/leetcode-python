from unittest import TestCase

from remove_all_adjacent_duplicates_in_string import remove_all_adjacent_duplicates_in_string


class Test(TestCase):
    def test_remove_all_adjacent_duplicates_in_string(self):
        self.assertEqual("ca", remove_all_adjacent_duplicates_in_string("abbaca"))
        self.assertEqual("ay", remove_all_adjacent_duplicates_in_string("azxxzy"))
        self.assertEqual("", remove_all_adjacent_duplicates_in_string("aa"))
        self.assertEqual("", remove_all_adjacent_duplicates_in_string("bcaacb"))
        self.assertEqual("c", remove_all_adjacent_duplicates_in_string("aac"))
