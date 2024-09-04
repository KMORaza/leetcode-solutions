from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        def build(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            root_index = inorder_index_map[root_val]
            left_size = root_index - in_start
            root.left = build(pre_start + 1, pre_start + left_size, in_start, root_index - 1)
            root.right = build(pre_start + left_size + 1, pre_end, root_index + 1, in_end)
            return root
        inorder_index_map = {value: idx for idx, value in enumerate(inorder)}
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
