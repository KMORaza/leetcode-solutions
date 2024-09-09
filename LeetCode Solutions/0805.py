from typing import List, Set
class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        total_sum = sum(nums)
        if not self.isPossible(total_sum, n):
            return False
        sums = [set() for _ in range(n // 2 + 1)]
        sums[0].add(0)
        for num in nums:
            for i in range(n // 2, 0, -1):
                for val in sums[i - 1]:
                    sums[i].add(num + val)
        for i in range(1, n // 2 + 1):
            if i * total_sum % n == 0 and (i * total_sum // n) in sums[i]:
                return True
        return False
    def isPossible(self, total_sum: int, n: int) -> bool:
        for i in range(1, n // 2 + 1):
            if i * total_sum % n == 0:
                return True
        return False
