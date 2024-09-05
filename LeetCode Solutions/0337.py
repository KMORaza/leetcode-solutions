class Solution:
    def rob(self, root):
        def dfs(node):
            if not node:
                return (0, 0)
            left = dfs(node.left)
            right = dfs(node.right)
            rob_this = node.val + left[0] + right[0]
            not_rob_this = max(left) + max(right)
            return (not_rob_this, rob_this)
        return max(dfs(root))
