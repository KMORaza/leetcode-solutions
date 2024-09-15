from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left_balance = dfs(node.left)
            right_balance = dfs(node.right)
            self.moves += abs(left_balance) + abs(right_balance)
            return node.val + left_balance + right_balance - 1
        dfs(root)
        return self.moves
