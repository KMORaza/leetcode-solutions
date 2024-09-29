class Solution:
    def minimumTime(self, obstacles: str) -> int:
        str_length = len(obstacles)
        cost_prefix = [0] * (str_length + 1)
        cost_suffix = [0] * (str_length + 1)
        for pos in range(str_length):
            if obstacles[pos] == '0':
                cost_prefix[pos + 1] = cost_prefix[pos]
            else:
                cost_prefix[pos + 1] = min(cost_prefix[pos] + 2, pos + 1)
        for pos in range(str_length - 1, -1, -1):
            if obstacles[pos] == '0':
                cost_suffix[pos] = cost_suffix[pos + 1]
            else:
                cost_suffix[pos] = min(cost_suffix[pos + 1] + 2, str_length - pos)
        min_removal_cost = float('inf')
        for pos in range(1, str_length + 1):
            min_removal_cost = min(min_removal_cost, cost_prefix[pos] + cost_suffix[pos])
        return min_removal_cost