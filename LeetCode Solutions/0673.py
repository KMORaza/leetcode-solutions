class Solution:
    def findNumberOfLIS(self, nums):
        if not nums:
            return 0
        n = len(nums)
        lengths = [1] * n
        counts = [1] * n
        for j in range(1, n):
            for i in range(j):
                if nums[i] < nums[j]:
                    if lengths[i] + 1 > lengths[j]:
                        lengths[j] = lengths[i] + 1
                        counts[j] = counts[i]
                    elif lengths[i] + 1 == lengths[j]:
                        counts[j] += counts[i]
        max_length = max(lengths)
        return sum(count for length, count in zip(lengths, counts) if length == max_length)
