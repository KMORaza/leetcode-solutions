from typing import List, Optional
from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        post_index_map = {val: i for i, val in enumerate(postorder)}
        def build_tree(pre_start, pre_end, post_start, post_end):
            if pre_start > pre_end or post_start > post_end:
                return None
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            if pre_start == pre_end:
                return root
            left_subtree_root_val = preorder[pre_start + 1]
            left_subtree_root_index_in_post = post_index_map[left_subtree_root_val]
            left_subtree_size = left_subtree_root_index_in_post - post_start + 1
            root.left = build_tree(pre_start + 1, pre_start + left_subtree_size, post_start, left_subtree_root_index_in_post)
            root.right = build_tree(pre_start + left_subtree_size + 1, pre_end, left_subtree_root_index_in_post + 1, post_end - 1)
            return root
        return build_tree(0, len(preorder) - 1, 0, len(postorder) - 1)
