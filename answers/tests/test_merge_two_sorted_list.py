from unittest import TestCase

from answers.common.list_utils import array_to_linked_list, compare_linked_list
from merge_two_sorted_list import merge_two_sorted_list


class Test(TestCase):
    def do_test_merge_two_sorted_list(self, expected, left, right):
        expected = array_to_linked_list(expected)
        left_list, right_list = array_to_linked_list(left), array_to_linked_list(right)
        self.assertTrue(compare_linked_list(expected, merge_two_sorted_list(left_list, right_list)))

    def test_merge_two_sorted_list(self):
        self.do_test_merge_two_sorted_list([1, 1, 2, 3, 4, 4], [1, 2, 4], [1, 3, 4])
        self.do_test_merge_two_sorted_list([], [], [])
        self.do_test_merge_two_sorted_list([1], [], [1])
        self.do_test_merge_two_sorted_list([1], [1], [])
        self.do_test_merge_two_sorted_list([1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1])
        self.do_test_merge_two_sorted_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                                           [2, 4, 6, 8, 10, 12, 14],
                                           [1, 3, 5, 7, 9, 11, 13, 15])
        self.do_test_merge_two_sorted_list([2, 4, 6, 8, 9, 10, 12, 14], [2, 4, 6, 8, 10, 12, 14], [9])
