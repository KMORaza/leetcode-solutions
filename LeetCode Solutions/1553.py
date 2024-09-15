from collections import deque
class Solution:
    def minDays(self, n: int) -> int:
        queue = deque([(n, 0)])
        visited = set()
        visited.add(n)
        while queue:
            current, days = queue.popleft()
            if current == 0:
                return days
            next_states = []
            if current % 2 == 0:
                next_states.append(current // 2)
            if current % 3 == 0:
                next_states.append(current // 3)
            next_states.append(current - 1)
            for next_state in next_states:
                if next_state >= 0 and next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, days + 1))
        return -1