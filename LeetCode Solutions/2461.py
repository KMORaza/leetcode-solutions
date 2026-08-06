class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k > n:
            return 0

        max_sum = 0
        current_sum = 0
        element_count = {}

        for i in range(k):
            current_sum += nums[i]
            element_count[nums[i]] = element_count.get(nums[i], 0) + 1

        if len(element_count) == k:
            max_sum = current_sum

        for i in range(k, n):
            left_element = nums[i - k]
            right_element = nums[i]

            current_sum = current_sum - left_element + right_element

            element_count[left_element] -= 1
            if element_count[left_element] == 0:
                del element_count[left_element]

            element_count[right_element] = element_count.get(right_element, 0) + 1

            if len(element_count) == k:
                max_sum = max(max_sum, current_sum)

        return max_sum