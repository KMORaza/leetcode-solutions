class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        self._push_left(root)
    def _push_left(self, node: TreeNode):
        while node:
            self.stack.append(node)
            node = node.left
    def next(self) -> int:
        node = self.stack.pop()
        value = node.val
        if node.right:
            self._push_left(node.right)
        return value
    def hasNext(self) -> bool:
        return len(self.stack) > 0