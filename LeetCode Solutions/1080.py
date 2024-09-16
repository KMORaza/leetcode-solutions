class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def sufficient(node: TreeNode, current_sum: int) -> Optional[TreeNode]:
            if not node:
                return None
            current_sum += node.val
            if not node.left and not node.right:
                if current_sum < limit:
                    return None
                else:
                    return node
            node.left = sufficient(node.left, current_sum)
            node.right = sufficient(node.right, current_sum)
            if not node.left and not node.right:
                return None
            return node
        return sufficient(root, 0)
