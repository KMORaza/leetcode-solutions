from collections import deque
from typing import List
class Solution:
    X = 50
    def getCoprimes(self, array: List[int], edgeList: List[List[int]]) -> List[int]:
        output = [-1] * len(array)
        graph = [[] for _ in range(len(array))]
        depthStacks = [[] for _ in range(self.X + 1)]
        for start, end in edgeList:
            graph[start].append(end)
            graph[end].append(start)
        self.traverse(graph, 0, -1, 0, array, depthStacks, output)
        return output
    def traverse(self, graph: List[List[int]], current: int, previous: int, level: int, array: List[int],
                 depthStacks: List[deque], output: List[int]):
        output[current] = self.findBestAncestor(current, depthStacks, array)
        depthStacks[array[current]].append((current, level))
        for neighbor in graph[current]:
            if neighbor != previous:
                self.traverse(graph, neighbor, current, level + 1, array, depthStacks, output)
        depthStacks[array[current]].pop()
    def findBestAncestor(self, current: int, depthStacks: List[deque], array: List[int]) -> int:
        bestNode = -1
        highestLevel = -1
        for i in range(1, self.X + 1):
            if depthStacks[i] and depthStacks[i][-1][1] > highestLevel and self.calculateGCD(array[current], i) == 1:
                bestNode = depthStacks[i][-1][0]
                highestLevel = depthStacks[i][-1][1]
        return bestNode
    def calculateGCD(self, a: int, b: int) -> int:
        return a if b == 0 else self.calculateGCD(b, a % b)
