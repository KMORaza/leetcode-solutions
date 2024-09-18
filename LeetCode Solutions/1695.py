class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        num_set = set()
        left = 0
        max_sum = 0
        current_sum = 0
        for right in range(len(nums)):
            while nums[right] in num_set:
                num_set.remove(nums[left])
                current_sum -= nums[left]
                left += 1
            num_set.add(nums[right])
            current_sum += nums[right]
            max_sum = max(max_sum, current_sum)
        return max_sum
