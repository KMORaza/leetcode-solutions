class Solution:
    def countPairsWithMaxDistance(self, nums: List[int], maxDist: int) -> int:
        count = 0
        j = 0
        n = len(nums)
        for i in range(n):
            while j < n and nums[j] - nums[i] <= maxDist:
                j += 1
            count += (j - i - 1)
        return count
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if self.countPairsWithMaxDistance(nums, mid) < k:
                left = mid + 1
            else:
                right = mid
        return left
