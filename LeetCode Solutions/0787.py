from typing import List
import math
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [math.inf] * n
        dist[src] = 0
        for _ in range(k + 1):
            temp_dist = dist.copy()
            for u, v, price in flights:
                if dist[u] < math.inf:
                    temp_dist[v] = min(temp_dist[v], dist[u] + price)
            dist = temp_dist
        return dist[dst] if dist[dst] < math.inf else -1
