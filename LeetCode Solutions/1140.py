class Solution:
    def stoneGameII(self, piles):
        size = len(piles)
        dp_table = [[-1] * (size + 1) for _ in range(size)]
        cumulative_sum = [0] * size
        cumulative_sum[-1] = piles[-1]
        for position in range(size - 2, -1, -1):
            cumulative_sum[position] = cumulative_sum[position + 1] + piles[position]
        return self._calculateMaxStones(cumulative_sum, 0, 1, dp_table)
    def _calculateMaxStones(self, cumulative_sum, position, current_max, dp_table):
        if position + 2 * current_max >= len(cumulative_sum):
            return cumulative_sum[position]
        if dp_table[position][current_max] != -1:
            return dp_table[position][current_max]
        min_opponent_score = cumulative_sum[position]
        for choice in range(1, 2 * current_max + 1):
            min_opponent_score = min(min_opponent_score, self._calculateMaxStones(cumulative_sum, position + choice, max(current_max, choice), dp_table))
        dp_table[position][current_max] = cumulative_sum[position] - min_opponent_score
        return dp_table[position][current_max]
