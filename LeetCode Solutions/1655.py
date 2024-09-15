from typing import List
from collections import Counter
class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        freq_list = self._calculate_frequencies(nums)
        valid_distributions = self._calculate_valid_distributions(freq_list, quantity)
        num_freqs = len(freq_list)
        num_quantities = len(quantity)
        max_bitmask = 1 << num_quantities
        dp_table = [[False] * max_bitmask for _ in range(num_freqs + 1)]
        dp_table[num_freqs][max_bitmask - 1] = True
        for i in range(num_freqs - 1, -1, -1):
            for bitmask in range(max_bitmask):
                dp_table[i][bitmask] = dp_table[i + 1][bitmask]
                remaining_mask = ~bitmask & (max_bitmask - 1)
                subset_mask = remaining_mask
                while subset_mask > 0:
                    if valid_distributions[i][subset_mask]:
                        dp_table[i][bitmask] = dp_table[i][bitmask] or dp_table[i + 1][bitmask | subset_mask]
                    subset_mask = (subset_mask - 1) & remaining_mask
        return dp_table[0][0]
    def _calculate_frequencies(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        return list(count.values())
    def _calculate_valid_distributions(self, freqs: List[int], quantity: List[int]) -> List[List[bool]]:
        max_bitmask = 1 << len(quantity)
        valid_distributions = [[False] * max_bitmask for _ in range(len(freqs))]
        for i in range(len(freqs)):
            for bitmask in range(max_bitmask):
                if freqs[i] >= self._compute_quantity_sum(quantity, bitmask):
                    valid_distributions[i][bitmask] = True
        return valid_distributions
    def _compute_quantity_sum(self, quantity: List[int], bitmask: int) -> int:
        total_quantity = 0
        for i in range(len(quantity)):
            if bitmask & (1 << i):
                total_quantity += quantity[i]
        return total_quantity
