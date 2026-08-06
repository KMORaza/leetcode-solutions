class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)

        def bfs(start):
            dist = [-1] * n
            dist[start] = 0
            curr = start
            d = 1
            while edges[curr] != -1:
                nxt = edges[curr]
                if dist[nxt] != -1:
                    break
                dist[nxt] = d
                d += 1
                curr = nxt
            return dist

        dist1 = bfs(node1)
        dist2 = bfs(node2)

        min_max_dist = float('inf')
        result = -1

        for i in range(n):
            if dist1[i] != -1 and dist2[i] != -1:
                max_dist = max(dist1[i], dist2[i])
                if max_dist < min_max_dist:
                    min_max_dist = max_dist
                    result = i

        return result