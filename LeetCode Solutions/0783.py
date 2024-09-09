from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        values = []
        def in_order_traversal(node: TreeNode):
            if node is None:
                return
            in_order_traversal(node.left)
            values.append(node.val)
            in_order_traversal(node.right)
        in_order_traversal(root)
        min_diff = float('inf')
        for i in range(1, len(values)):
            min_diff = min(min_diff, values[i] - values[i - 1])
        return min_diff
