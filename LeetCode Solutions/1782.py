from collections import defaultdict
from bisect import bisect_right
class Solution:
    def countPairs(self, total_nodes: int, connections: list[list[int]], thresholds: list[int]) -> list[int]:
        results = [0] * len(thresholds)
        degree = [0] * (total_nodes + 1)
        edge_count = [defaultdict(int) for _ in range(total_nodes + 1)]
        for node_a, node_b in connections:
            degree[node_a] += 1
            degree[node_b] += 1
            edge_count[min(node_a, node_b)][max(node_a, node_b)] += 1
        sorted_degree = sorted(degree[1:])
        query_index = 0
        for threshold in thresholds:
            left, right = 0, total_nodes - 1
            while left < right:
                if sorted_degree[left] + sorted_degree[right] > threshold:
                    results[query_index] += (right - left)
                    right -= 1
                else:
                    left += 1
            for node in range(1, total_nodes + 1):
                for adjacent, shared_edges in edge_count[node].items():
                    if degree[node] + degree[adjacent] > threshold and degree[node] + degree[adjacent] - shared_edges <= threshold:
                        results[query_index] -= 1
            query_index += 1
        return results
