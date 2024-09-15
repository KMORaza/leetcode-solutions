from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val > root.val:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        def insert_into_right_subtree(node: TreeNode, val: int) -> TreeNode:
            if not node.right or val > node.right.val:
                new_node = TreeNode(val)
                new_node.left = node.right
                node.right = new_node
                return root
            insert_into_right_subtree(node.right, val)
            return root
        return insert_into_right_subtree(root, val)
