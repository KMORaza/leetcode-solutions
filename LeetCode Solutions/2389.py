class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + nums[i]

        result = []
        for q in queries:
            left, right = 0, n
            while left <= right:
                mid = (left + right) // 2
                if prefix_sums[mid] <= q:
                    left = mid + 1
                else:
                    right = mid - 1
            result.append(right)

        return result