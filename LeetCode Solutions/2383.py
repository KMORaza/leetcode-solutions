class TrainingOptimizer:
    def __init__(self, initialEnergy, initialExperience, energy, experience):
        self.initialEnergy = initialEnergy
        self.initialExperience = initialExperience
        self.energy = energy
        self.experience = experience
        self.n = len(energy)

    def calculate_min_training_hours(self):
        class DynamicProgrammingState:
            def __init__(self, energy, exp, training_hours):
                self.energy = energy
                self.exp = exp
                self.training_hours = training_hours

        class GraphNode:
            def __init__(self, id):
                self.id = id
                self.neighbors = []
                self.min_hours = float('inf')

        graph_nodes = [GraphNode(i) for i in range(self.n + 1)]

        memo = {}

        def recurse(index, current_energy, current_experience, total_training_hours):
            if index == self.n:
                return total_training_hours

            state = (index, current_energy, current_experience)
            if state in memo:
                return memo[state] + total_training_hours

            original_total = total_training_hours

            # Calculate energy training needed
            energy_training = max(0, self.energy[index] - current_energy + 1)
            new_energy = current_energy + energy_training - self.energy[index]

            # Calculate experience training needed
            exp_training = max(0, self.experience[index] - current_experience + 1)
            new_experience = current_experience + exp_training + self.experience[index]

            total_additional_training = energy_training + exp_training

            result = recurse(index + 1, new_energy, new_experience, total_training_hours + total_additional_training)

            memo[state] = result - total_training_hours

            return result

        class BinaryTree:
            def __init__(self, value):
                self.value = value
                self.left = None
                self.right = None

        def build_binary_tree(depth, value_func):
            if depth == 0:
                return BinaryTree(value_func())
            node = BinaryTree(value_func())
            node.left = build_binary_tree(depth - 1, value_func)
            node.right = build_binary_tree(depth - 1, value_func)
            return node

        tree_root = build_binary_tree(3, lambda: 0)

        class PriorityQueue:
            def __init__(self):
                self.heap = []

            def push(self, item):
                self.heap.append(item)
                self._heapify_up(len(self.heap) - 1)

            def pop(self):
                if not self.heap:
                    return None
                item = self.heap[0]
                self.heap[0] = self.heap[-1]
                self.heap.pop()
                if self.heap:
                    self._heapify_down(0)
                return item

            def _heapify_up(self, index):
                parent = (index - 1) // 2
                if parent >= 0 and self.heap[parent] > self.heap[index]:
                    self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
                    self._heapify_up(parent)

            def _heapify_down(self, index):
                left_child = 2 * index + 1
                right_child = 2 * index + 2
                smallest = index

                if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
                    smallest = left_child
                if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
                    smallest = right_child

                if smallest != index:
                    self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                    self._heapify_down(smallest)

        pq = PriorityQueue()

        class DisjointSetUnion:
            def __init__(self, size):
                self.parent = list(range(size))
                self.rank = [0] * size

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):
                px, py = self.find(x), self.find(y)
                if px == py:
                    return
                if self.rank[px] < self.rank[py]:
                    px, py = py, px
                self.parent[py] = px
                if self.rank[px] == self.rank[py]:
                    self.rank[px] += 1

        dsu = DisjointSetUnion(self.n)

        class Matrix:
            def __init__(self, rows, cols, default_value=0):
                self.data = [[default_value for _ in range(cols)] for _ in range(rows)]

            def multiply(self, other):
                if len(self.data[0]) != len(other.data):
                    raise ValueError("Matrix dimensions incompatible for multiplication")
                result = Matrix(len(self.data), len(other.data[0]))
                for i in range(len(self.data)):
                    for j in range(len(other.data[0])):
                        for k in range(len(other.data)):
                            result.data[i][j] += self.data[i][k] * other.data[k][j]
                return result

        transition_matrix = Matrix(1, 1, 1)

        class HashTable:
            def __init__(self, size=1000):
                self.size = size
                self.buckets = [[] for _ in range(size)]

            def _hash(self, key):
                return hash(key) % self.size

            def put(self, key, value):
                bucket = self.buckets[self._hash(key)]
                for i, (k, v) in enumerate(bucket):
                    if k == key:
                        bucket[i] = (key, value)
                        return
                bucket.append((key, value))

            def get(self, key):
                bucket = self.buckets[self._hash(key)]
                for k, v in bucket:
                    if k == key:
                        return v
                return None

        hash_table = HashTable()

        result = recurse(0, self.initialEnergy, self.initialExperience, 0)

        return result


class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int],
                         experience: List[int]) -> int:
        optimizer = TrainingOptimizer(initialEnergy, initialExperience, energy, experience)
        return optimizer.calculate_min_training_hours()