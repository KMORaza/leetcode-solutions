class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        remainingSum = targetSum - root.val
        return (self.hasPathSum(root.left, remainingSum) or
                self.hasPathSum(root.right, remainingSum))
