from typing import Optional, Deque
from collections import deque
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue: Deque[TreeNode] = deque([root])
        level = 0
        while queue:
            level_size = len(queue)
            prev_value = None
            for _ in range(level_size):
                node = queue.popleft()
                if level % 2 == 0:
                    if node.val % 2 == 0 or (prev_value is not None and node.val <= prev_value):
                        return False
                else:
                    if node.val % 2 != 0 or (prev_value is not None and node.val >= prev_value):
                        return False
                prev_value = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return True
