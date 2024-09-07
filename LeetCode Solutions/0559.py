from typing import List, Optional
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
class Solution:
    def maxDepth(self, root: Optional[Node]) -> int:
        if not root:
            return 0
        def dfs(node):
            if not node.children:
                return 1
            return 1 + max(dfs(child) for child in node.children)
        return dfs(root)
