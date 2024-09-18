class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        bitmask = 0
        first_occurrence = {0: -1}
        max_length = 0
        for i, char in enumerate(s):
            if char == 'a':
                bitmask ^= 1 << 0
            elif char == 'e':
                bitmask ^= 1 << 1
            elif char == 'i':
                bitmask ^= 1 << 2
            elif char == 'o':
                bitmask ^= 1 << 3
            elif char == 'u':
                bitmask ^= 1 << 4
            if bitmask in first_occurrence:
                length = i - first_occurrence[bitmask]
                max_length = max(max_length, length)
            else:
                first_occurrence[bitmask] = i
        return max_length
