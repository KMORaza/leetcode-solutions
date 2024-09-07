class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def in_order_traversal(node):
            if node is None:
                return
            in_order_traversal(node.left)
            values.append(node.val)
            in_order_traversal(node.right)
        values = []
        in_order_traversal(root)
        min_diff = float('inf')
        for i in range(1, len(values)):
            min_diff = min(min_diff, values[i] - values[i - 1])
        return min_diff