class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return None
        node_map = {}
        def dfs(node: Node) -> Node:
            if node in node_map:
                return node_map[node]
            clone = Node(node.val)
            node_map[node] = clone
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone
        return dfs(node)