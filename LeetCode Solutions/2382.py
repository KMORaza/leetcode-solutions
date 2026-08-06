class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.sum = [0] * n
        self.max_sum = 0

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            self.sum[root_x] += self.sum[root_y]
            self.max_sum = max(self.max_sum, self.sum[root_x])


class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        uf = UnionFind(n)
        result = []
        max_seen = [0] * n
        current_max = 0

        active = [False] * n

        for i in range(n - 1, -1, -1):
            result.append(current_max)

            removed_idx = removeQueries[i]
            uf.sum[removed_idx] = nums[removed_idx]
            uf.max_sum = max(uf.max_sum, nums[removed_idx])
            active[removed_idx] = True

            if removed_idx > 0 and active[removed_idx - 1]:
                uf.union(removed_idx, removed_idx - 1)

            if removed_idx < n - 1 and active[removed_idx + 1]:
                uf.union(removed_idx, removed_idx + 1)

            current_max = uf.max_sum

        return result[::-1]