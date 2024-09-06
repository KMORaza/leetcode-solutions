from collections import deque
from typing import List, Optional
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
class Solution:
    def levelOrder(self, root: Optional[Node]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            level_values = []
            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)
                for child in node.children:
                    queue.append(child)
            result.append(level_values)
        return result
