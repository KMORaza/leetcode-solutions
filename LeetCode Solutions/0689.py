class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        subarray_sum = [0] * (n - k + 1)
        current_sum = sum(nums[:k])
        subarray_sum[0] = current_sum
        for i in range(1, n - k + 1):
            current_sum = current_sum - nums[i - 1] + nums[i + k - 1]
            subarray_sum[i] = current_sum
        left_max = [0] * (n - k + 1)
        left_max[0] = 0
        for i in range(1, n - k + 1):
            if subarray_sum[i] > subarray_sum[left_max[i - 1]]:
                left_max[i] = i
            else:
                left_max[i] = left_max[i - 1]
        right_max = [0] * (n - k + 1)
        right_max[n - k] = n - k
        for i in range(n - k - 1, -1, -1):
            if subarray_sum[i] >= subarray_sum[right_max[i + 1]]:
                right_max[i] = i
            else:
                right_max[i] = right_max[i + 1]
        max_sum = 0
        result = []
        for j in range(k, n - 2 * k + 1):
            i = left_max[j - k]
            l = right_max[j + k]
            total_sum = subarray_sum[i] + subarray_sum[j] + subarray_sum[l]
            if total_sum > max_sum:
                max_sum = total_sum
                result = [i, j, l]
        return result
