class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if not root or (not root.left and not root.right):
            return False
        left_val = root.left.val if root.left else 0
        right_val = root.right.val if root.right else 0
        return left_val + right_val == root.val