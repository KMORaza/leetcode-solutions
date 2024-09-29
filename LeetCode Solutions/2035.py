from collections import defaultdict
from bisect import bisect_left
class Solution:
    def minimumDifference(self, array):
        half_length = len(array) // 2
        subset_sums_first = defaultdict(set)
        subset_sums_second = defaultdict(set)
        for bitmask in range(1 << half_length):
            total_first = 0
            count_first = 0
            total_second = 0
            count_second = 0
            for idx in range(half_length):
                if (bitmask & (1 << idx)) != 0:
                    total_first += array[idx]
                    count_first += 1
                    total_second += array[half_length + idx]
                    count_second += 1
                else:
                    total_first -= array[idx]
                    total_second -= array[half_length + idx]
            subset_sums_first[count_first].add(total_first)
            subset_sums_second[count_second].add(total_second)
        smallest_difference = float('inf')
        for elements_count in range(half_length + 1):
            sorted_first_sums = sorted(subset_sums_first[elements_count])
            sorted_second_sums = sorted(subset_sums_second[half_length - elements_count])
            for first_sum in sorted_first_sums:
                target_sum = -first_sum
                pos = bisect_left(sorted_second_sums, target_sum)
                if pos < len(sorted_second_sums):
                    smallest_difference = min(smallest_difference, abs(first_sum + sorted_second_sums[pos]))
                if pos > 0:
                    smallest_difference = min(smallest_difference, abs(first_sum + sorted_second_sums[pos - 1]))
        return smallest_difference
