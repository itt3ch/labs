import unittest
import sys
sys.path.append('../src')
from binary_leaves import BinaryTree, branch_sums


class TestBranchSums(unittest.TestCase):
    def test_single_root_in_tree(self):
        root = BinaryTree(5)
        expected_result = 0
        self.assertEqual(branch_sums(root), expected_result)

    def test_for_all_roots(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        root.right.left = BinaryTree(15)
        root.right.right = BinaryTree(7)
        expected_result = 7

        self.assertEqual(branch_sums(root), expected_result)