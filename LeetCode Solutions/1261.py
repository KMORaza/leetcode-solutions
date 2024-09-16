from typing import Optional, Set
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.values = set()
        if root:
            self._recover_tree(root, 0)
    def _recover_tree(self, node: TreeNode, value: int):
        if not node:
            return
        node.val = value
        self.values.add(value)
        if node.left:
            self._recover_tree(node.left, 2 * value + 1)
        if node.right:
            self._recover_tree(node.right, 2 * value + 2)
    def find(self, target: int) -> bool:
        return target in self.values