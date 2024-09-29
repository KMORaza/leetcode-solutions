from typing import List
from collections import deque
class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        if start == goal:
            return 0
        visited = set()
        queue = deque([(start, 0)])
        visited.add(start)
        while queue:
            current, steps = queue.popleft()
            for num in nums:
                for next_num in (current + num, current - num, current ^ num):
                    if next_num == goal:
                        return steps + 1
                    if 0 <= next_num <= 1000 and next_num not in visited:
                        visited.add(next_num)
                        queue.append((next_num, steps + 1))
        return -1