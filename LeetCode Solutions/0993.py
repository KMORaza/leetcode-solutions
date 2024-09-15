from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        x_info = y_info = None
        def dfs(node: TreeNode, depth: int, parent: TreeNode) -> None:
            nonlocal x_info, y_info
            if not node:
                return
            if node.val == x:
                x_info = (depth, parent)
            elif node.val == y:
                y_info = (depth, parent)
            if node.left:
                dfs(node.left, depth + 1, node)
            if node.right:
                dfs(node.right, depth + 1, node)
        dfs(root, 0, None)
        if x_info and y_info:
            x_depth, x_parent = x_info
            y_depth, y_parent = y_info
            return x_depth == y_depth and x_parent != y_parent
        return False
