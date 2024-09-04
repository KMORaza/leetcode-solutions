class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def is_valid_bst(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return (is_valid_bst(node.left, low, node.val) and
                    is_valid_bst(node.right, node.val, high))
        return is_valid_bst(root, float('-inf'), float('inf'))
