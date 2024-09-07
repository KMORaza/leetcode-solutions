from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
            if not tree1 and not tree2:
                return True
            if not tree1 or not tree2 or tree1.val != tree2.val:
                return False
            return isSameTree(tree1.left, tree2.left) and isSameTree(tree1.right, tree2.right)
        def isSubtreeHelper(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            if not root:
                return False
            if isSameTree(root, subRoot):
                return True
            return isSubtreeHelper(root.left, subRoot) or isSubtreeHelper(root.right, subRoot)
        return isSubtreeHelper(root, subRoot)
