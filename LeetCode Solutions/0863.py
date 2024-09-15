from typing import List
from collections import deque, defaultdict
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        def build_graph(node: TreeNode, parent: TreeNode):
            if not node:
                return
            if parent:
                graph[node].append(parent)
                graph[parent].append(node)
            build_graph(node.left, node)
            build_graph(node.right, node)
        build_graph(root, None)
        result = []
        visited = set()
        queue = deque([(target, 0)])
        visited.add(target)
        while queue:
            node, dist = queue.popleft()
            if dist == k:
                result.append(node.val)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
        return result
