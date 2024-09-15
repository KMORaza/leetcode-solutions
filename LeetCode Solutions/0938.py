class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0
            total_sum = 0
            if low <= node.val <= high:
                total_sum += node.val
            if node.val > low:
                total_sum += dfs(node.left)
            if node.val < high:
                total_sum += dfs(node.right)
            return total_sum
        return dfs(root)
