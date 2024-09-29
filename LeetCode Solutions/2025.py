from collections import defaultdict
class Solution:
    def waysToPartition(self, elements, adjustment):
        size = len(elements)
        total_sum = sum(elements)
        running_total = 0
        left_map = defaultdict(int)
        right_map = defaultdict(int)
        for idx in range(1, size):
            running_total += elements[idx - 1]
            remaining = total_sum - running_total
            right_map[running_total - remaining] += 1
        max_partitions = right_map.get(0, 0)
        running_total = 0
        for current in elements:
            required_change = adjustment - current
            max_partitions = max(max_partitions, left_map.get(required_change, 0) + right_map.get(-required_change, 0))
            running_total += current
            remaining = total_sum - running_total
            balance = running_total - remaining
            right_map[balance] -= 1
            left_map[balance] += 1
        return max_partitions