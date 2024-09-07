class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.total_tilt = 0
    def findTilt(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            tilt = abs(left_sum - right_sum)
            self.total_tilt += tilt
            return node.val + left_sum + right_sum
        dfs(root)
        return self.total_tilt