from collections import deque
from typing import Optional
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = deque([root])
        found_gap = False
        while queue:
            node = queue.popleft()
            if node:
                if found_gap:
                    return False
                queue.append(node.left)
                queue.append(node.right)
            else:
                found_gap = True
        return True