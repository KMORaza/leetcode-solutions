class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def is_same(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return is_same(p.left, q.left) and is_same(p.right, q.right)
        return is_same(p, q)