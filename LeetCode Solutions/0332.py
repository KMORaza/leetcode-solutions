from collections import defaultdict
import heapq
class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph = defaultdict(list)
        for src, dest in tickets:
            heapq.heappush(graph[src], dest)
        result = []
        def dfs(airport):
            while graph[airport]:
                next_airport = heapq.heappop(graph[airport])
                dfs(next_airport)
            result.append(airport)
        dfs("JFK")
        return result[::-1]