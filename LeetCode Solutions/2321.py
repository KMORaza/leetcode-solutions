class Solution:
    def maximumsSplicedArray(self, nums1, nums2):
        n = len(nums1)

        # Calculate initial sums
        sum1 = sum(nums1)
        sum2 = sum(nums2)

        # Find max gain for swapping to improve nums1
        diff = [nums2[i] - nums1[i] for i in range(n)]
        max_gain1 = 0
        current_sum = 0
        for d in diff:
            current_sum = max(d, current_sum + d)
            max_gain1 = max(max_gain1, current_sum)

        # Find max gain for swapping to improve nums2
        diff = [nums1[i] - nums2[i] for i in range(n)]
        max_gain2 = 0
        current_sum = 0
        for d in diff:
            current_sum = max(d, current_sum + d)
            max_gain2 = max(max_gain2, current_sum)

        # Calculate maximum possible score
        return max(sum1 + max_gain1, sum2 + max_gain2)