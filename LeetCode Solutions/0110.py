from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkBalance(node: Optional[TreeNode]) -> (int, bool):
            if not node:
                return 0, True
            left_height, left_balanced = checkBalance(node.left)
            right_height, right_balanced = checkBalance(node.right)
            balanced = (left_balanced and right_balanced and abs(left_height - right_height) <= 1)
            height = max(left_height, right_height) + 1
            return height, balanced
        _, is_balanced = checkBalance(root)
        return is_balanced