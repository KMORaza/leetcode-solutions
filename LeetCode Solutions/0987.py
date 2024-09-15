from collections import defaultdict, deque
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        node_map = defaultdict(list)
        queue = deque([(root, 0, 0)])
        while queue:
            node, vert_dist, hor_dist = queue.popleft()
            node_map[vert_dist].append((hor_dist, node.val))
            if node.left:
                queue.append((node.left, vert_dist - 1, hor_dist + 1))
            if node.right:
                queue.append((node.right, vert_dist + 1, hor_dist + 1))
        result = []
        for vert_dist in sorted(node_map.keys()):
            column_nodes = sorted(node_map[vert_dist], key=lambda x: (x[0], x[1]))
            result.append([val for _, val in column_nodes])
        return result
