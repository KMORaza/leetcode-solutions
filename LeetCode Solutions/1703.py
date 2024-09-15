class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        ones_positions = [i for i, num in enumerate(nums) if num == 1]
        ones_count = len(ones_positions)
        if k > ones_count:
            return 0
        min_cost = float('inf')
        for i in range(ones_count - k + 1):
            segment = ones_positions[i:i + k]
            median_index = k // 2
            median = segment[median_index]
            cost = 0
            for j, pos in enumerate(segment):
                cost += abs(pos - (median - median_index + j))
            min_cost = min(min_cost, cost)
        return min_cost
