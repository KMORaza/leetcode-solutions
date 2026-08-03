class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        from collections import Counter
        count = Counter(nums)
        pairs = 0
        leftover = 0
        for freq in count.values():
            pairs += freq // 2
            leftover += freq % 2
        return [pairs, leftover]