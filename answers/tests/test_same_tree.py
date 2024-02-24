from unittest import TestCase

from answers.common.TreeNode import construct_tree
from same_tree import same_tree


class Test(TestCase):
    def test_same_tree(self):
        self.assertEqual(True, same_tree(construct_tree([1, 2, 3]), construct_tree([1, 2, 3])))
        self.assertEqual(False, same_tree(construct_tree([1, 2]), construct_tree([1, None, 2])))
        self.assertEqual(False, same_tree(construct_tree([1, 2, 1]), construct_tree([1, 1, 2])))
        self.assertEqual(True, same_tree(construct_tree([1]), construct_tree([1])))
        self.assertEqual(True, same_tree(construct_tree([1, 2, 3, 4, 5, 6, 7, 8, 9]),
                                         construct_tree([1, 2, 3, 4, 5, 6, 7, 8, 9])))
