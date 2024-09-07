class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, root: TreeNode) -> str:
        def dfs(node):
            if not node:
                return ""
            result = str(node.val)
            if node.left or node.right:
                left_str = dfs(node.left)
                right_str = dfs(node.right)
                result += f"({left_str})"
                if node.right:
                    result += f"({right_str})"
            return result
        return dfs(root)
