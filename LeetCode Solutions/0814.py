class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def containsOne(node: TreeNode) -> bool:
            if not node:
                return False
            left_contains_one = containsOne(node.left)
            right_contains_one = containsOne(node.right)
            if not left_contains_one:
                node.left = None
            if not right_contains_one:
                node.right = None
            return node.val == 1 or left_contains_one or right_contains_one
        return root if containsOne(root) else None
