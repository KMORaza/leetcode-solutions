class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return self._calculate_sum(root, 1, 1)
    def _calculate_sum(self, node: TreeNode, parent_val: int, grandparent_val: int) -> int:
        if node is None:
            return 0
        current_sum = node.val if grandparent_val % 2 == 0 else 0
        current_sum += self._calculate_sum(node.left, node.val, parent_val)
        current_sum += self._calculate_sum(node.right, node.val, parent_val)
        return current_sum
