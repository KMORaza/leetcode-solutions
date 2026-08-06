class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        max_length = 1
        current_length = 1
        n = len(s)

        for i in range(1, n):
            if ord(s[i]) == ord(s[i - 1]) + 1:
                current_length += 1
                max_length = max(max_length, current_length)
            else:
                current_length = 1

        return max_length