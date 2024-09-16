from collections import deque
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        queue = deque([(1, 1)])
        visited = set()
        visited.add(1)
        while queue:
            remainder, length = queue.popleft()
            if remainder % k == 0:
                return length
            next_remainder1 = (remainder * 10 + 1) % k
            if next_remainder1 not in visited:
                visited.add(next_remainder1)
                queue.append((next_remainder1, length + 1))
        return -1