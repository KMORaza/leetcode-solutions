from typing import List
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        connection_count = [0] * n
        for a, b in roads:
            connection_count[a] += 1
            connection_count[b] += 1
        city_connections = list(enumerate(connection_count))
        city_connections.sort(key=lambda x: x[1], reverse=True)
        value_assignment = [0] * n
        for value, (city, _) in enumerate(city_connections, start=1):
            value_assignment[city] = n - value + 1
        total_importance = 0
        for a, b in roads:
            total_importance += value_assignment[a] + value_assignment[b]
        return total_importance
