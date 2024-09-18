class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        import heapq
        from collections import defaultdict
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        def dijkstra(start):
            min_heap = [(0, start)]
            distances = [float('inf')] * n
            distances[start] = 0
            while min_heap:
                d, u = heapq.heappop(min_heap)
                if d > distances[u]:
                    continue
                for v, w in graph[u]:
                    if d + w < distances[v]:
                        distances[v] = d + w
                        heapq.heappush(min_heap, (distances[v], v))
            return distances
        min_count, city_with_min_neighbors = float('inf'), -1
        for i in range(n):
            distances = dijkstra(i)
            count = sum(1 for d in distances if d <= distanceThreshold)
            if count <= min_count:
                min_count = count
                city_with_min_neighbors = i
        return city_with_min_neighbors
