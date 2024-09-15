class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size))
    def search(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.search(self.parent[x])
        return self.parent[x]
    def merge(self, a, b):
        rootA = self.search(a)
        rootB = self.search(b)
        if rootA != rootB:
            self.parent[rootA] = rootB
class Solution:
    def largestComponentSize(self, nums):
        max_value = max(nums)
        disjoint_set = DisjointSet(max_value + 1)
        for num in nums:
            for factor in range(2, int(num**0.5) + 1):
                if num % factor == 0:
                    disjoint_set.merge(num, factor)
                    disjoint_set.merge(num, num // factor)
        count = [0] * (max_value + 1)
        max_component_size = 0
        for num in nums:
            root = disjoint_set.search(num)
            count[root] += 1
            max_component_size = max(max_component_size, count[root])
        return max_component_size
