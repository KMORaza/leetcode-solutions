class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num
            if prefix_sum > 0:
                count += 1
            else:
                break

        return count