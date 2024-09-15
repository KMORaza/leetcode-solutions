from collections import deque
class Solution:
    def isEscapePossible(self, blocked, source, target):
        def bfs(start, end):
            if start == end:
                return True
            queue = deque([start])
            visited = set([tuple(start)])
            while queue:
                x, y = queue.popleft()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < 10**6 and 0 <= ny < 10**6 and (nx, ny) not in blocked_set
                            and (nx, ny) not in visited):
                        if [nx, ny] == end:
                            return True
                        queue.append((nx, ny))
                        visited.add((nx, ny))
                        if len(visited) >= 20000:
                            return True
            return False
        blocked_set = set(tuple(b) for b in blocked)
        if len(blocked) < 2:
            return True
        return bfs(source, target) and bfs(target, source)
