from collections import deque, defaultdict
import sys
class Solution:
    def secondMinimum(self, n: int, edges: list[list[int]], time: int, change: int) -> int:
        adjacency_map = defaultdict(list)
        traversal_queue = deque([(1, 0)])
        time_records = [[sys.maxsize] * 2 for _ in range(n + 1)]
        time_records[1][0] = 0
        for source, target in edges:
            adjacency_map[source].append(target)
            adjacency_map[target].append(source)
        while traversal_queue:
            current_vertex, prior_duration = traversal_queue.popleft()
            signal_cycles = prior_duration // change
            delay_duration = 0 if signal_cycles % 2 == 0 else change - prior_duration % change
            new_duration = prior_duration + delay_duration + time
            for adjacent_vertex in adjacency_map[current_vertex]:
                if new_duration < time_records[adjacent_vertex][0]:
                    time_records[adjacent_vertex][0] = new_duration
                    traversal_queue.append((adjacent_vertex, new_duration))
                elif time_records[adjacent_vertex][0] < new_duration < time_records[adjacent_vertex][1]:
                    if adjacent_vertex == n:
                        return new_duration
                    time_records[adjacent_vertex][1] = new_duration
                    traversal_queue.append((adjacent_vertex, new_duration))
        raise ValueError("No valid path found")
