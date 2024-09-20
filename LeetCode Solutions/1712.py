class Solution:
    def waysToSplit(self, nums):
        length = len(nums)
        result = 0
        cumulative_sum = nums[:]
        for index in range(1, length):
            cumulative_sum[index] += cumulative_sum[index - 1]
        for index in range(length - 2):
            first_index = self.findFirstGreaterEqual(cumulative_sum, index)
            if first_index == length - 1:
                break
            mid_sum = cumulative_sum[first_index] - cumulative_sum[index]
            right_sum = cumulative_sum[-1] - cumulative_sum[first_index]
            if mid_sum > right_sum:
                continue
            last_index = self.findFirstGreater(cumulative_sum, index)
            result = (result + last_index - first_index) % (10**9+7)
        return result
    def findFirstGreaterEqual(self, cumulative_sum, index):
        left, right = index + 1, len(cumulative_sum) - 1
        while left < right:
            mid = (left + right) // 2
            if cumulative_sum[mid] - cumulative_sum[index] >= cumulative_sum[index]:
                right = mid
            else:
                left = mid + 1
        return left
    def findFirstGreater(self, cumulative_sum, index):
        left, right = index + 1, len(cumulative_sum) - 1
        while left < right:
            mid = (left + right) // 2
            if cumulative_sum[mid] - cumulative_sum[index] > cumulative_sum[-1] - cumulative_sum[mid]:
                right = mid
            else:
                left = mid + 1
        return left
