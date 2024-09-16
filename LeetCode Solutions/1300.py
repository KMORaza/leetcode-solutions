class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        def compute_sum(val):
            return sum(min(x, val) for x in arr)
        left, right = 0, max(arr)
        while left < right:
            mid = (left + right) // 2
            if compute_sum(mid) <= target:
                left = mid + 1
            else:
                right = mid
        if abs(compute_sum(left - 1) - target) <= abs(compute_sum(left) - target):
            return left - 1
        return left
