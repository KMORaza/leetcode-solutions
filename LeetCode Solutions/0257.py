from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node: TreeNode, path: str, paths: List[str]):
            if node:
                path += str(node.val)
                if not node.left and not node.right:
                    paths.append(path)
                else:
                    path += '->'
                    if node.left:
                        dfs(node.left, path, paths)
                    if node.right:
                        dfs(node.right, path, paths)
        paths = []
        dfs(root, '', paths)
        return paths