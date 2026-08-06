class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        from collections import defaultdict

        n = len(nums)
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        total_sum = sum(nums)
        target_divisors = []
        for i in range(1, int(total_sum ** 0.5) + 1):
            if total_sum % i == 0:
                target_divisors.append(i)
                if i != total_sum // i:
                    target_divisors.append(total_sum // i)

        target_divisors.sort()

        def dfs(node, parent, target):
            current_sum = nums[node]
            for neighbor in graph[node]:
                if neighbor != parent:
                    child_sum = dfs(neighbor, node, target)
                    if child_sum == -1:
                        return -1
                    current_sum += child_sum

            if current_sum > target:
                return -1
            if current_sum == target:
                return 0
            return current_sum

        for target in target_divisors:
            components = total_sum // target
            if dfs(0, -1, target) == 0:
                return components - 1

        return 0