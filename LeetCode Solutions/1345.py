from collections import deque, defaultdict
from typing import List
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        value_to_indices = defaultdict(list)
        for i, value in enumerate(arr):
            value_to_indices[value].append(i)
        queue = deque([0])
        jumps = 0
        visited = set([0])
        while queue:
            size = len(queue)
            for _ in range(size):
                current = queue.popleft()
                if current == n - 1:
                    return jumps
                for neighbor in value_to_indices[arr[current]]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                value_to_indices[arr[current]] = []
                if current - 1 >= 0 and current - 1 not in visited:
                    visited.add(current - 1)
                    queue.append(current - 1)
                if current + 1 < n and current + 1 not in visited:
                    visited.add(current + 1)
                    queue.append(current + 1)
            jumps += 1
        return -1