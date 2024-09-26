class GraphNode:
    def __init__(self):
        self.kids = []
        self.locked_by_id = -1
class LockingTree:
    def __init__(self, ancestry):
        self.ancestry = ancestry
        self.graph_nodes = [GraphNode() for _ in range(len(ancestry))]
        for idx in range(1, len(ancestry)):
            self.graph_nodes[ancestry[idx]].kids.append(idx)
    def lock(self, node_id, user_id):
        if self.graph_nodes[node_id].locked_by_id != -1:
            return False
        self.graph_nodes[node_id].locked_by_id = user_id
        return True
    def unlock(self, node_id, user_id):
        if self.graph_nodes[node_id].locked_by_id != user_id:
            return False
        self.graph_nodes[node_id].locked_by_id = -1
        return True
    def upgrade(self, node_id, user_id):
        if self.graph_nodes[node_id].locked_by_id != -1:
            return False
        if not self.has_locked_descendant(node_id):
            return False
        current_node = node_id
        while current_node != -1:
            if self.graph_nodes[current_node].locked_by_id != -1:
                return False
            current_node = self.ancestry[current_node]
        self.release_all_descendants(node_id)
        self.graph_nodes[node_id].locked_by_id = user_id
        return True
    def has_locked_descendant(self, current_index):
        if self.graph_nodes[current_index].locked_by_id != -1:
            return True
        return any(self.has_locked_descendant(child) for child in self.graph_nodes[current_index].kids)
    def release_all_descendants(self, current_index):
        self.graph_nodes[current_index].locked_by_id = -1
        for child in self.graph_nodes[current_index].kids:
            self.release_all_descendants(child)