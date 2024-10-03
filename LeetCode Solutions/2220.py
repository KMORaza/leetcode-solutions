class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        differing_bits = start ^ goal
        return bin(differing_bits).count('1')
