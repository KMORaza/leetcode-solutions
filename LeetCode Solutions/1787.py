from collections import defaultdict
from typing import List
class Solution:
    def minChanges(self, input_array: List[int], num_groups: int) -> int:
        x = 1 << 10
        segment_counts = [defaultdict(int) for _ in range(num_groups)]
        segment_sizes = [0] * num_groups
        for idx, elem in enumerate(input_array):
            segment_counts[idx % num_groups][elem] += 1
            segment_sizes[idx % num_groups] += 1
        change_counts = [float('inf')] * x
        change_counts[0] = 0
        for group_index in range(num_groups):
            new_change_counts = [min(change_counts) + segment_sizes[group_index]] * x
            for xor_value in range(x):
                for number, count in segment_counts[group_index].items():
                    new_change_counts[xor_value] = min(new_change_counts[xor_value],
                                                         change_counts[xor_value ^ number] +
                                                         segment_sizes[group_index] - count)
            change_counts = new_change_counts
        return change_counts[0]
