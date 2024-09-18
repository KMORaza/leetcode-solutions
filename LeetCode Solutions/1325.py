class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def remove(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return None
            node.left = remove(node.left)
            node.right = remove(node.right)
            if not node.left and not node.right and node.val == target:
                return None
            return node
        return remove(root)
