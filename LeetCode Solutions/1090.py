from typing import List
from collections import defaultdict
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        items = sorted(zip(values, labels), key=lambda x: -x[0])
        label_usage = defaultdict(int)
        total_sum = 0
        items_selected = 0
        for value, label in items:
            if items_selected >= numWanted:
                break
            if label_usage[label] < useLimit:
                total_sum += value
                label_usage[label] += 1
                items_selected += 1
        return total_sum
