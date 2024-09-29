from collections import defaultdict
from typing import List, Tuple
class Solution:
    def minimumOperations(self, input_nums: List[int]) -> int:
        self.num_array = input_nums
        self.total_length = len(input_nums)
        least_operations = float('inf')
        even_stats = self.compute_frequency(0)
        odd_stats = self.compute_frequency(1)
        for even_value, even_frequency in even_stats:
            for odd_value, odd_frequency in odd_stats:
                if even_value != odd_value:
                    least_operations = min(least_operations, self.total_length - (even_frequency + odd_frequency))
        return least_operations
    def compute_frequency(self, start_index: int) -> List[Tuple[int, int]]:
        count_map = defaultdict(int)
        for index in range(start_index, self.total_length, 2):
            count_map[self.num_array[index]] += 1
        first_value = first_count = 0
        second_value = second_count = 0
        for key, value in count_map.items():
            if value > first_count:
                second_value, second_count = first_value, first_count
                first_value, first_count = key, value
            elif value > second_count:
                second_value, second_count = key, value
        return [(first_value, first_count), (second_value, second_count)]
