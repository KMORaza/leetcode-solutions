class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        n = len(nums)
        pairs = [(nums[i], cost[i]) for i in range(n)]
        pairs.sort()

        total_cost = sum(cost)
        median_pos = (total_cost + 1) // 2

        current_sum = 0
        target = 0
        for num, c in pairs:
            current_sum += c
            if current_sum >= median_pos:
                target = num
                break

        result = 0
        for i in range(n):
            result += abs(nums[i] - target) * cost[i]

        return result