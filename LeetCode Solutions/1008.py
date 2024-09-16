from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def build_tree(lower=float('-inf'), upper=float('inf')):
            nonlocal index
            if index >= len(preorder):
                return None
            val = preorder[index]
            if val < lower or val > upper:
                return None
            index += 1
            root = TreeNode(val)
            root.left = build_tree(lower, val)
            root.right = build_tree(val, upper)
            return root
        index = 0
        return build_tree()
