from collections import deque
from typing import List, Tuple
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0])
        def bfs(start: Tuple[int, int], end: Tuple[int, int]) -> int:
            if start == end:
                return 0
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            queue = deque([start])
            visited = set([start])
            steps = 0
            while queue:
                for _ in range(len(queue)):
                    x, y = queue.popleft()
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if (0 <= nx < m and 0 <= ny < n and
                            (nx, ny) not in visited and forest[nx][ny] != 0):
                            if (nx, ny) == end:
                                return steps + 1
                            queue.append((nx, ny))
                            visited.add((nx, ny))
                steps += 1
            return -1
        trees = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    trees.append((forest[i][j], i, j))
        trees.sort()
        start = (0, 0)
        total_steps = 0
        for height, x, y in trees:
            steps = bfs(start, (x, y))
            if steps == -1:
                return -1
            total_steps += steps
            start = (x, y)
        return total_steps
