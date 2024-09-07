class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: TreeNode):
        from collections import defaultdict
        def in_order_traversal(node):
            if not node:
                return
            in_order_traversal(node.left)
            count[node.val] += 1
            in_order_traversal(node.right)
        count = defaultdict(int)
        in_order_traversal(root)
        max_count = max(count.values(), default=0)
        modes = [value for value, freq in count.items() if freq == max_count]
        return modes
