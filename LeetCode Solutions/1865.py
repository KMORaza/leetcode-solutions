from collections import defaultdict
from typing import List
class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.count_map = defaultdict(int)
        for num in nums2:
            self.count_map[num] += 1
    def add(self, index: int, val: int) -> None:
        old_value = self.nums2[index]
        self.nums2[index] += val
        self.count_map[old_value] -= 1
        if self.count_map[old_value] == 0:
            del self.count_map[old_value]
        self.count_map[self.nums2[index]] += 1
    def count(self, tot: int) -> int:
        total_pairs = 0
        for num in self.nums1:
            complement = tot - num
            total_pairs += self.count_map[complement]
        return total_pairs
