class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        def inorder(node: TreeNode):
            if node:
                inorder(node.left)
                nodes.append(node)
                inorder(node.right)
        inorder(root)
        dummy = TreeNode(-1)
        current = dummy
        for node in nodes:
            node.left = None
            current.right = node
            current = node
        return dummy.right
