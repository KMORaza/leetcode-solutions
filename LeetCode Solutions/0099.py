class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            self.traversal.append(node)
            inorder(node.right)
        self.traversal = []
        inorder(root)
        x = y = None
        for i in range(len(self.traversal) - 1):
            if self.traversal[i].val > self.traversal[i + 1].val:
                y = self.traversal[i + 1]
                if x is None:
                    x = self.traversal[i]
                else:
                    break
        if x and y:
            x.val, y.val = y.val, x.val
