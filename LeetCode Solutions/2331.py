class Solution:
    def evaluateTree(self, root):
        if root.val == 0:
            return False
        if root.val == 1:
            return True
        left_val = self.evaluateTree(root.left)
        right_val = self.evaluateTree(root.right)
        if root.val == 2:
            return left_val or right_val
        return left_val and right_val