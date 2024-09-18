class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node, direction, length):
            if not node:
                return
            nonlocal max_length
            max_length = max(max_length, length)
            if direction == 'left':
                dfs(node.left, 'left', 1)
                dfs(node.right, 'right', length + 1)
            else:
                dfs(node.right, 'right', 1)
                dfs(node.left, 'left', length + 1)
        max_length = 0
        dfs(root, 'left', 0)
        dfs(root, 'right', 0)
        return max_length
