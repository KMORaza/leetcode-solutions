class Solution:
    def maxValueAfterReverse(self, nums):
        total_diff = 0
        min_value = float('inf')
        max_value = float('-inf')
        for index in range(len(nums) - 1):
            current = nums[index]
            next_value = nums[index + 1]
            diff = (current - next_value) if (current - next_value) >= 0 else (next_value - current)
            total_diff += diff
            min_value = min(min_value, max(current, next_value))
            max_value = max(max_value, min(current, next_value))
        additional_diff = max(0, (max_value - min_value) * 2)
        for index in range(len(nums) - 1):
            current = nums[index]
            next_value = nums[index + 1]
            head_contribution = -((current - next_value) if (current - next_value) >= 0 else (next_value - current)) + \
                                ((nums[0] - next_value) if (nums[0] - next_value) >= 0 else (next_value - nums[0]))
            tail_contribution = -((current - next_value) if (current - next_value) >= 0 else (next_value - current)) + \
                                ((nums[-1] - current) if (nums[-1] - current) >= 0 else (current - nums[-1]))
            additional_diff = max(additional_diff, max(head_contribution, tail_contribution))
        return total_diff + additional_diff
