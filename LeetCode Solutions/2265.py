class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0
        def helper(node):
            if not node:
                return (0, 0)
            left_sum, left_count = helper(node.left)
            right_sum, right_count = helper(node.right)
            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1
            if total_count > 0 and total_sum // total_count == node.val:
                self.count += 1
            return (total_sum, total_count)
        helper(root)
        return self.count
