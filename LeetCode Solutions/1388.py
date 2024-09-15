class Solution:
    def __init__(self):
        self.num_picks = 0
    def maxSizeSlices(self, slices):
        self.num_picks = len(slices) // 3
        slices_excluding_first = slices[1:]
        max_sum_without_first = self._compute_max_sum(slices_excluding_first)
        slices_excluding_last = slices[:-1]
        max_sum_without_last = self._compute_max_sum(slices_excluding_last)
        return max(max_sum_without_first, max_sum_without_last)
    def _compute_max_sum(self, array):
        array_length = len(array)
        dp_table = [[0] * (self.num_picks + 1) for _ in range(array_length + 1)]
        for index in range(1, array_length + 1):
            for picks in range(1, self.num_picks + 1):
                dp_table[index][picks] = max(
                    dp_table[index - 1][picks],
                    (dp_table[index - 2][picks - 1] if index >= 2 else 0) + array[index - 1])
        return dp_table[array_length][self.num_picks]
