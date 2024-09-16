from typing import Optional
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_sum = float('-inf')
        max_level = 0
        current_level = 1
        queue = deque([root])
        while queue:
            level_size = len(queue)
            current_sum = 0
            for _ in range(level_size):
                node = queue.popleft()
                current_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if current_sum > max_sum:
                max_sum = current_sum
                max_level = current_level
            current_level += 1
        return max_level
