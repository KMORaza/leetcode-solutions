class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(node: TreeNode, min_val: int, max_val: int) -> int:
            if not node:
                return max_val - min_val
            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)
            left_diff = helper(node.left, min_val, max_val)
            right_diff = helper(node.right, min_val, max_val)
            return max(left_diff, right_diff)
        if not root:
            return 0
        return helper(root, root.val, root.val)
