from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def isUnival(root: Optional[TreeNode], value: int) -> bool:
            if root is None:
                return True
            if root.val != value:
                return False
            return isUnival(root.left, value) and isUnival(root.right, value)
        if root is None:
            return True
        return isUnival(root, root.val)
