from collections import deque
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class CBTInserter:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.queue = deque()
        q = deque([root])
        while q:
            node = q.popleft()
            if not node.left or not node.right:
                self.queue.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    def insert(self, val: int) -> int:
        parent = self.queue[0]
        new_node = TreeNode(val)
        if not parent.left:
            parent.left = new_node
        else:
            parent.right = new_node
            self.queue.popleft()
        self.queue.append(new_node)
        return parent.val
    def get_root(self) -> Optional[TreeNode]:
        return self.root
