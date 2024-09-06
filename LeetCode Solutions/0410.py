class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def canSplit(max_sum: int) -> bool:
            current_sum = 0
            count = 1
            for num in nums:
                if current_sum + num > max_sum:
                    count += 1
                    current_sum = num
                    if count > k:
                        return False
                else:
                    current_sum += num
            return True
        low, high = max(nums), sum(nums)
        while low < high:
            mid = (low + high) // 2
            if canSplit(mid):
                high = mid
            else:
                low = mid + 1
        return low