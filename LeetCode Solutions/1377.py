from collections import deque, defaultdict
from typing import List
class Solution:
    def frogPosition(self, num_nodes: int, edges_list: List[List[int]], time_limit: int, target_node: int) -> float:
        adjacency_list = defaultdict(list)
        for start, end in edges_list:
            adjacency_list[start].append(end)
            adjacency_list[end].append(start)
        queue = deque([1])
        visited = [False] * (num_nodes + 1)
        probabilities = [0.0] * (num_nodes + 1)
        visited[1] = True
        probabilities[1] = 1.0
        while queue and time_limit > 0:
            level_size = len(queue)
            time_limit -= 1
            for _ in range(level_size):
                current_node = queue.popleft()
                child_count = 0
                for neighbor in adjacency_list[current_node]:
                    if not visited[neighbor]:
                        child_count += 1
                for neighbor in adjacency_list[current_node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        probabilities[neighbor] = probabilities[current_node] / child_count
                        queue.append(neighbor)
                if child_count > 0:
                    probabilities[current_node] = 0.0
        return probabilities[target_node]
