class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branch_sums(root):
    if root is None:
        return 0

    if root.right is not None:
        if root.right.right is None and root.right.left is None:
            return root.right.value + branch_sums(root.left)

    return branch_sums(root.left) + branch_sums(root.right)