class Solution:
    def maxNumber(self, nums1, nums2, k):
        def max_single_number(nums, length):
            stack = []
            drop = len(nums) - length
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:length]
        def merge(nums1, nums2):
            return [max(nums1, nums2).pop(0) for _ in range(len(nums1) + len(nums2))]
        max_result = []
        for i in range(max(0, k - len(nums2)), min(len(nums1), k) + 1):
            part1 = max_single_number(nums1, i)
            part2 = max_single_number(nums2, k - i)
            max_result = max(max_result, merge(part1, part2))
        return max_result
