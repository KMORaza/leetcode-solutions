from collections import Counter
class Solution:
    def findLHS(self, nums: list[int]) -> int:
        count = Counter(nums)
        max_length = 0
        for num in count:
            if num + 1 in count:
                length = count[num] + count[num + 1]
                max_length = max(max_length, length)
        return max_length

