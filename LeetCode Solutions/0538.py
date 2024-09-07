class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def reverse_in_order(node: TreeNode):
            nonlocal total_sum
            if not node:
                return
            reverse_in_order(node.right)
            total_sum += node.val
            node.val = total_sum
            reverse_in_order(node.left)
        total_sum = 0
        reverse_in_order(root)
        return root