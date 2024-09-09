from collections import deque, defaultdict
class Solution:
    def shortestPathLength(self, graph):
        n = len(graph)
        if n == 1:
            return 0
        queue = deque()
        visited = set()
        for i in range(n):
            start_mask = 1 << i
            queue.append((i, start_mask, 0))
            visited.add((i, start_mask))
        while queue:
            current_node, visited_mask, distance = queue.popleft()
            if visited_mask == (1 << n) - 1:
                return distance
            for neighbor in graph[current_node]:
                new_visited_mask = visited_mask | (1 << neighbor)
                if (neighbor, new_visited_mask) not in visited:
                    visited.add((neighbor, new_visited_mask))
                    queue.append((neighbor, new_visited_mask, distance + 1))
        return -1