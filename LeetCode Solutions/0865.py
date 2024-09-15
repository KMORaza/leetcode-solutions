class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return (0, None)
            left_depth, left_subtree = dfs(node.left)
            right_depth, right_subtree = dfs(node.right)
            if left_depth == right_depth:
                return (left_depth + 1, node)
            if left_depth > right_depth:
                return (left_depth + 1, left_subtree)
            else:
                return (right_depth + 1, right_subtree)
        _, subtree = dfs(root)
        return subtree
