from typing import List
from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        queue = deque([start])
        visited = [False] * n
        visited[start] = True
        while queue:
            index = queue.popleft()
            if arr[index] == 0:
                return True
            jump = arr[index]
            next_positions = [index + jump, index - jump]
            for next_index in next_positions:
                if 0 <= next_index < n and not visited[next_index]:
                    visited[next_index] = True
                    queue.append(next_index)
        return False
