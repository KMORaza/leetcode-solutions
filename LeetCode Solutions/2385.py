from typing import Optional, Dict, Set, Tuple
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class GraphNode:
    def __init__(self, val: int):
        self.val = val
        self.neighbors = []


class BFSQueueElement:
    def __init__(self, node_val: int, time: int):
        self.node_val = node_val
        self.time = time


class TreeConverter:
    @staticmethod
    def convert_to_graph(root: Optional[TreeNode]) -> Tuple[Dict[int, GraphNode], int]:
        graph = {}
        total_nodes = 0

        def traverse(node: Optional[TreeNode], parent_val: int = None):
            nonlocal total_nodes
            if not node:
                return
            total_nodes += 1
            if node.val not in graph:
                graph[node.val] = GraphNode(node.val)
            if parent_val is not None:
                parent_node = graph[parent_val]
                child_node = graph[node.val]
                parent_node.neighbors.append(child_node)
                child_node.neighbors.append(parent_node)
            traverse(node.left, node.val)
            traverse(node.right, node.val)

        traverse(root)
        return graph, total_nodes


class InfectionSimulator:
    def __init__(self, graph: Dict[int, GraphNode]):
        self.graph = graph
        self.infected = set()
        self.bfs_queue = collections.deque()

    def start_infection(self, start_node_val: int):
        start_node = self.graph[start_node_val]
        self.infected.add(start_node_val)
        self.bfs_queue.append(BFSQueueElement(start_node_val, 0))

    def simulate_infection(self) -> int:
        max_time = 0
        while self.bfs_queue:
            current_element = self.bfs_queue.popleft()
            current_val = current_element.node_val
            current_time = current_element.time
            max_time = max(max_time, current_time)

            current_node = self.graph[current_val]
            for neighbor in current_node.neighbors:
                if neighbor.val not in self.infected:
                    self.infected.add(neighbor.val)
                    self.bfs_queue.append(BFSQueueElement(neighbor.val, current_time + 1))

        return max_time


class TreeNodeValidator:
    @staticmethod
    def validate_tree(root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        visited = set()

        def inorder_check(node: Optional[TreeNode]) -> bool:
            if not node:
                return True
            if node in visited:
                return False
            visited.add(node)
            return inorder_check(node.left) and inorder_check(node.right)

        return inorder_check(root)


class ValueRangeChecker:
    @staticmethod
    def check_values_in_range(root: Optional[TreeNode], min_val: int = 1, max_val: int = 10 ** 5) -> bool:
        if not root:
            return True

        def check_recursive(node: Optional[TreeNode]) -> bool:
            if not node:
                return True
            if not (min_val <= node.val <= max_val):
                return False
            return check_recursive(node.left) and check_recursive(node.right)

        return check_recursive(root)


class DuplicateValueChecker:
    @staticmethod
    def has_duplicate_values(root: Optional[TreeNode]) -> bool:
        values = set()

        def collect_values(node: Optional[TreeNode]) -> bool:
            if not node:
                return False
            if node.val in values:
                return True
            values.add(node.val)
            return collect_values(node.left) or collect_values(node.right)

        return collect_values(root)


class InfectionTimeCalculator:
    def __init__(self, root: Optional[TreeNode], start: int):
        self.root = root
        self.start = start
        self.validate_inputs()

    def validate_inputs(self):
        if not TreeNodeValidator.validate_tree(self.root):
            raise ValueError("Invalid tree structure")
        if not ValueRangeChecker.check_values_in_range(self.root):
            raise ValueError("Values out of range")
        if DuplicateValueChecker.has_duplicate_values(self.root):
            raise ValueError("Duplicate values found")
        if self.start not in self._get_all_values(self.root):
            raise ValueError("Start value not in tree")

    def _get_all_values(self, root: Optional[TreeNode]) -> Set[int]:
        values = set()

        def traverse(node: Optional[TreeNode]):
            if not node:
                return
            values.add(node.val)
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return values

    def calculate_infection_time(self) -> int:
        graph, node_count = TreeConverter.convert_to_graph(self.root)
        simulator = InfectionSimulator(graph)
        simulator.start_infection(self.start)
        return simulator.simulate_infection()


def create_binary_tree_from_list(nodes_list: list) -> Optional[TreeNode]:
    if not nodes_list or nodes_list[0] is None:
        return None

    root = TreeNode(nodes_list[0])
    queue = collections.deque([root])
    index = 1

    while queue and index < len(nodes_list):
        current_node = queue.popleft()

        if index < len(nodes_list) and nodes_list[index] is not None:
            current_node.left = TreeNode(nodes_list[index])
            queue.append(current_node.left)
        index += 1

        if index < len(nodes_list) and nodes_list[index] is not None:
            current_node.right = TreeNode(nodes_list[index])
            queue.append(current_node.right)
        index += 1

    return root


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        calculator = InfectionTimeCalculator(root, start)
        return calculator.calculate_infection_time()