class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return
            unique_values.add(node.val)
            dfs(node.left)
            dfs(node.right)
        unique_values = set()
        dfs(root)
        min_val = root.val
        second_min_val = float('inf')
        for value in unique_values:
            if min_val < value < second_min_val:
                second_min_val = value
        return second_min_val if second_min_val != float('inf') else -1
