from functools import lru_cache
from math import comb
from typing import List, Tuple, Dict
class Solution:
    def __init__(self):
        self.total_half_balls = 0
        self.binomial_matrix = []
        self.ball_counts = []
        self.memo: Dict[Tuple[int, int, int], int] = {}
    def getProbability(self, balls: List[int]) -> float:
        max_count = 0
        self.total_half_balls = 0
        for count in balls:
            self.total_half_balls += count
            max_count = max(max_count, count)
        self.total_half_balls //= 2
        self.ball_counts = balls
        matrix_dim = max(max_count, self.total_half_balls * 2)
        self.binomial_matrix = [[0] * (matrix_dim + 1) for _ in range(matrix_dim + 1)]
        for i in range(matrix_dim + 1):
            self.binomial_matrix[i][0] = 1
            for j in range(1, i + 1):
                self.binomial_matrix[i][j] = (self.binomial_matrix[i - 1][j - 1] +
                                              self.binomial_matrix[i - 1][j])
        valid_count = self._search(0, self.total_half_balls, 0)
        total_count = self.binomial_matrix[self.total_half_balls * 2][self.total_half_balls]
        return valid_count / total_count
    def _search(self, idx: int, remaining: int, color_diff: int) -> int:
        if idx >= len(self.ball_counts):
            return 1 if remaining == 0 and color_diff == 0 else 0
        if remaining < 0:
            return 0
        key = (idx, remaining, color_diff)
        if key in self.memo:
            return self.memo[key]
        valid_count = 0
        for x in range(self.ball_counts[idx] + 1):
            diff_adjustment = (1 if x == self.ball_counts[idx] else -1 if x == 0 else 0)
            valid_count += (self._search(idx + 1, remaining - x, color_diff + diff_adjustment) *
                            self.binomial_matrix[self.ball_counts[idx]][x])
        self.memo[key] = valid_count
        return valid_count
