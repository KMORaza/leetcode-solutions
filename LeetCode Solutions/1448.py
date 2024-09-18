class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, max_val: int) -> int:
            if not node:
                return 0
            good_count = 1 if node.val >= max_val else 0
            new_max_val = max(max_val, node.val)
            good_count += dfs(node.left, new_max_val)
            good_count += dfs(node.right, new_max_val)
            return good_count
        return dfs(root, float('-inf'))
