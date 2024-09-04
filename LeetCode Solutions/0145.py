class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        result_stack = []
        traversal_stack = [root]
        while traversal_stack:
            node = traversal_stack.pop()
            result_stack.append(node.val)
            if node.left:
                traversal_stack.append(node.left)
            if node.right:
                traversal_stack.append(node.right)
        return result_stack[::-1]
