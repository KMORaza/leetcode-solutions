from typing import List, Deque, Tuple
from collections import deque, defaultdict
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph_red = defaultdict(list)
        graph_blue = defaultdict(list)
        for u, v in redEdges:
            graph_red[u].append(v)
        for u, v in blueEdges:
            graph_blue[u].append(v)
        distances = [[-1] * n for _ in range(2)]
        distances[0][0] = 0
        distances[1][0] = 0
        queue: Deque[Tuple[int, int]] = deque([(0, 0), (0, 1)])
        while queue:
            node, color = queue.popleft()
            next_color = 1 - color
            neighbors = graph_red[node] if next_color == 0 else graph_blue[node]
            for neighbor in neighbors:
                if distances[next_color][neighbor] == -1:
                    distances[next_color][neighbor] = distances[color][node] + 1
                    queue.append((neighbor, next_color))
        result = []
        for i in range(n):
            dist_red = distances[0][i]
            dist_blue = distances[1][i]
            if dist_red == -1 and dist_blue == -1:
                result.append(-1)
            elif dist_red == -1:
                result.append(dist_blue)
            elif dist_blue == -1:
                result.append(dist_red)
            else:
                result.append(min(dist_red, dist_blue))
        return result
