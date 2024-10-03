import heapq
from collections import defaultdict
from typing import List, Tuple
class Solution:
    x=10**10
    def minimumWeight(self, nodeCount: int, edgeList: List[List[int]], source1: int, source2: int, target: int) -> int:
        adjacencyList = defaultdict(list)
        reverseAdjacencyList = defaultdict(list)
        for start, end, weight in edgeList:
            adjacencyList[start].append((end, weight))
            reverseAdjacencyList[end].append((start, weight))
        distancesFromSource1 = self.dijkstra(adjacencyList, source1, nodeCount)
        distancesFromSource2 = self.dijkstra(adjacencyList, source2, nodeCount)
        distancesFromTarget = self.dijkstra(reverseAdjacencyList, target, nodeCount)
        minimumPathWeight = self.x
        for index in range(nodeCount):
            if (distancesFromSource1[index] == self.x or
                distancesFromSource2[index] == self.x or
                distancesFromTarget[index] == self.x):
                continue
            minimumPathWeight = min(minimumPathWeight, distancesFromSource1[index] + distancesFromSource2[index] + distancesFromTarget[index])
        return -1 if minimumPathWeight == self.x else minimumPathWeight
    def dijkstra(self, graph: defaultdict, startNode: int, nodeCount: int) -> List[int]:
        distanceArray = [self.x] * nodeCount
        distanceArray[startNode] = 0
        priorityQueue = [(0, startNode)]
        while priorityQueue:
            currentDistance, currentNode = heapq.heappop(priorityQueue)
            if currentDistance > distanceArray[currentNode]:
                continue
            for neighbor, weight in graph[currentNode]:
                if currentDistance + weight < distanceArray[neighbor]:
                    distanceArray[neighbor] = currentDistance + weight
                    heapq.heappush(priorityQueue, (distanceArray[neighbor], neighbor))
        return distanceArray
