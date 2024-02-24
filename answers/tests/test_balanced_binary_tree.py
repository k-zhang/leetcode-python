from unittest import TestCase

from answers.common.TreeNode import construct_tree
from balanced_binary_tree import is_balanced


class TestBalancedBinaryTree(TestCase):
    def test_dfs(self):
        self.assertEqual(True, is_balanced(construct_tree([3, 9, 20, None, None, 15, 7])))
        self.assertEqual(True, is_balanced(construct_tree([3, 9, 20, None, None, None, 7])))
        self.assertEqual(False, is_balanced(construct_tree([3, 9, 20, None, None, None, 7, 8, None])))
        self.assertEqual(False, is_balanced(construct_tree([1, 2, 2, 3, 3, None, None, 4, 4])))
        self.assertEqual(False, is_balanced(construct_tree([1, 2, 2, 3, 3, None, None, 4, 4])))
        self.assertEqual(False, is_balanced(construct_tree([1, 2, 2, 3, 3, None, None, 4, 4])))
        self.assertEqual(True, is_balanced(construct_tree([])))
