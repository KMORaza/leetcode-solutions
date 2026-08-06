# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        total_swaps = 0

        while queue:
            level_size = len(queue)
            level_values = []

            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if len(level_values) <= 1:
                continue

            sorted_values = sorted(level_values)
            value_to_index = {val: idx for idx, val in enumerate(sorted_values)}

            visited = [False] * len(level_values)
            swaps = 0

            for i in range(len(level_values)):
                if visited[i] or level_values[i] == sorted_values[i]:
                    continue

                cycle_length = 0
                current = i

                while not visited[current]:
                    visited[current] = True
                    current = value_to_index[level_values[current]]
                    cycle_length += 1

                if cycle_length > 1:
                    swaps += cycle_length - 1

            total_swaps += swaps

        return total_swaps