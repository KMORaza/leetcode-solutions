class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        from collections import defaultdict

        n = len(nums)
        graph = defaultdict(set)

        for i in range(n):
            for j in range(i + 1, n):
                if abs(nums[i] - nums[j]) == k:
                    graph[i].add(j)
                    graph[j].add(i)

        count = 0

        for mask in range(1, 1 << n):
            valid = True
            for i in range(n):
                if mask & (1 << i):
                    for j in graph[i]:
                        if mask & (1 << j):
                            valid = False
                            break
                    if not valid:
                        break
            if valid:
                count += 1

        return count