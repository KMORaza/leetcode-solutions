class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], bitmask: int) -> int:
            if not node:
                return 0
            bitmask ^= (1 << node.val)
            if not node.left and not node.right:
                return 1 if bitmask & (bitmask - 1) == 0 else 0
            left_paths = dfs(node.left, bitmask)
            right_paths = dfs(node.right, bitmask)
            return left_paths + right_paths
        return dfs(root, 0)
