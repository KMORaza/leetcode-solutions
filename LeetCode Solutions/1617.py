import sys
import itertools
class Solution:
    def countSubgraphsForEachDiameter(self, num_vertices, edges):
        total_masks = 1 << num_vertices
        shortest_paths = self.calculateShortestPaths(num_vertices, edges)
        result = [0] * (num_vertices - 1)
        for subset_mask in range(total_masks):
            largest_distance = self.calculateMaxDistance(subset_mask, shortest_paths, num_vertices)
            if largest_distance > 0:
                result[largest_distance - 1] += 1
        return result
    def calculateShortestPaths(self, num_vertices, graph_edges):
        distances = [[num_vertices] * num_vertices for _ in range(num_vertices)]
        for i in range(num_vertices):
            distances[i][i] = 0
        for start, end in graph_edges:
            start -= 1
            end -= 1
            distances[start][end] = 1
            distances[end][start] = 1
        for intermediate in range(num_vertices):
            for source in range(num_vertices):
                for destination in range(num_vertices):
                    distances[source][destination] = min(distances[source][destination], distances[source][intermediate] + distances[intermediate][destination])
        return distances
    def calculateMaxDistance(self, subset_mask, distances, num_vertices):
        largest_distance = 0
        total_edges = 0
        total_cities = 0
        for u in range(num_vertices):
            if not (subset_mask & (1 << u)):
                continue
            total_cities += 1
            for v in range(u + 1, num_vertices):
                if not (subset_mask & (1 << v)):
                    continue
                if distances[u][v] == 1:
                    total_edges += 1
                largest_distance = max(largest_distance, distances[u][v])
        return largest_distance if total_edges == total_cities - 1 else 0
