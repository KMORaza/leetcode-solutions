class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def dfs(node, current_sum):
            if not node:
                return 0
            current_sum += node.val
            path_count = prefix_sum_count.get(current_sum - targetSum, 0)
            prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1
            path_count += dfs(node.left, current_sum)
            path_count += dfs(node.right, current_sum)
            prefix_sum_count[current_sum] -= 1
            return path_count
        prefix_sum_count = {0: 1}
        return dfs(root, 0)
