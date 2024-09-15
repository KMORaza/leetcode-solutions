class Solution:
    def countTriplets(self, nums):
        max_val = max(nums, default=0)
        count = [0] * (max_val + 1)
        for x in nums:
            for y in nums:
                count[x & y] += 1
        answer = 0
        for xy in range(max_val + 1):
            for z in nums:
                if (xy & z) == 0:
                    answer += count[xy]
        return answer
