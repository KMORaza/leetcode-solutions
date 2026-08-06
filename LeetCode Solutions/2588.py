class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        from collections import defaultdict

        prefix_xor = 0
        count = 0
        freq = defaultdict(int)
        freq[0] = 1

        for num in nums:
            prefix_xor ^= num
            count += freq[prefix_xor]
            freq[prefix_xor] += 1

        return count