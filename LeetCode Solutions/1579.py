class DisjointSet:
    def __init__(self, total_nodes):
        self.parent_nodes = list(range(total_nodes))
        self.set_sizes = [1] * total_nodes
        self.total_sets = total_nodes
    def find_parent(self, node):
        if self.parent_nodes[node] != node:
            self.parent_nodes[node] = self.find_parent(self.parent_nodes[node])
        return self.parent_nodes[node]
    def merge_sets(self, node1, node2):
        root1 = self.find_parent(node1)
        root2 = self.find_parent(node2)
        if root1 == root2:
            return False
        if self.set_sizes[root1] > self.set_sizes[root2]:
            self.parent_nodes[root2] = root1
            self.set_sizes[root1] += self.set_sizes[root2]
        else:
            self.parent_nodes[root1] = root2
            self.set_sizes[root2] += self.set_sizes[root1]
        self.total_sets -= 1
        return True
class Solution:
    def maxNumEdgesToRemove(self, node_count, edge_list):
        alice_ds = DisjointSet(node_count)
        bob_ds = DisjointSet(node_count)
        redundant_edges = 0
        for edge in edge_list:
            edge_type, node1, node2 = edge
            if edge_type == 3:
                if not alice_ds.merge_sets(node1 - 1, node2 - 1):
                    redundant_edges += 1
                else:
                    bob_ds.merge_sets(node1 - 1, node2 - 1)
        for edge in edge_list:
            edge_type, node1, node2 = edge
            if edge_type == 1 and not alice_ds.merge_sets(node1 - 1, node2 - 1):
                redundant_edges += 1
            if edge_type == 2 and not bob_ds.merge_sets(node1 - 1, node2 - 1):
                redundant_edges += 1
        return redundant_edges if alice_ds.total_sets == 1 and bob_ds.total_sets == 1 else -1
