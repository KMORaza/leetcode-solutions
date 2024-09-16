class Solution:
    def btreeGameWinningMove(self, root: TreeNode, total_nodes: int, target_value: int) -> bool:
        target_node = self.findTargetNode(root, target_value)
        if not target_node:
            return False
        left_subtree_size = self.countSubtreeNodes(target_node.left)
        right_subtree_size = self.countSubtreeNodes(target_node.right)
        remaining_subtree_size = total_nodes - left_subtree_size - right_subtree_size - 1
        return max(left_subtree_size, right_subtree_size, remaining_subtree_size) > total_nodes / 2
    def findTargetNode(self, root: TreeNode, target_value: int) -> TreeNode:
        if root is None or root.val == target_value:
            return root
        left_result = self.findTargetNode(root.left, target_value)
        return left_result if left_result is not None else self.findTargetNode(root.right, target_value)
    def countSubtreeNodes(self, node: TreeNode) -> int:
        if node is None:
            return 0
        return 1 + self.countSubtreeNodes(node.left) + self.countSubtreeNodes(node.right)
