from typing import List
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def canAchieve(target: int) -> bool:
            operations = 0
            for num in nums:
                if num > target:
                    operations += (num - 1) // target
            return operations <= maxOperations
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if canAchieve(mid):
                right = mid
            else:
                left = mid + 1
        return left
