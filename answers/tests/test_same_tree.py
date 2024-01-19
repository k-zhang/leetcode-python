from unittest import TestCase

from answers.common.tree_node import TreeNode
from same_tree import same_tree


class Test(TestCase):
    def test_same_tree(self):
        self.assertEqual(True, same_tree(TreeNode([1, 2, 3]), TreeNode([1, 2, 3])))
        self.assertEqual(False, same_tree(TreeNode([1, 2]), TreeNode([1, None, 2])))
        self.assertEqual(False, same_tree(TreeNode([1, 2, 1]), TreeNode([1, 1, 2])))
        self.assertEqual(True, same_tree(TreeNode([1]), TreeNode([1])))
        self.assertEqual(True, same_tree(TreeNode([1, 2, 3, 4, 5, 6, 7, 8, 9]), TreeNode([1, 2, 3, 4, 5, 6, 7, 8, 9])))
