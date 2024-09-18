from typing import List
from collections import defaultdict, deque
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        if n == 0:
            return True
        parent = [-1] * n
        adj = defaultdict(list)
        for node in range(n):
            if leftChild[node] != -1:
                if parent[leftChild[node]] != -1:
                    return False
                parent[leftChild[node]] = node
                adj[node].append(leftChild[node])
            if rightChild[node] != -1:
                if parent[rightChild[node]] != -1:
                    return False
                parent[rightChild[node]] = node
                adj[node].append(rightChild[node])
        root_count = 0
        for i in range(n):
            if parent[i] == -1:
                root_count += 1
                root = i
        if root_count != 1:
            return False
        visited = [False] * n
        queue = deque([root])
        visited[root] = True
        visited_count = 0
        while queue:
            node = queue.popleft()
            visited_count += 1
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return visited_count == n
