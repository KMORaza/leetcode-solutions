from collections import deque
from typing import List
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden_set = set(forbidden)
        max_position = max(x + a + b, max(forbidden) + a + b)
        visited = set()
        queue = deque([(0, 0, True)])
        visited.add((0, True))
        while queue:
            position, jumps, can_jump_back = queue.popleft()
            if position == x:
                return jumps
            next_forward = position + a
            if next_forward not in forbidden_set and next_forward <= max_position:
                if (next_forward, True) not in visited:
                    visited.add((next_forward, True))
                    queue.append((next_forward, jumps + 1, True))
            if can_jump_back:
                next_backward = position - b
                if next_backward >= 0 and next_backward not in forbidden_set:
                    if (next_backward, False) not in visited:
                        visited.add((next_backward, False))
                        queue.append((next_backward, jumps + 1, False))
        return -1
